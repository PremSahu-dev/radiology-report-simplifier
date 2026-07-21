// part -1
/*=========================================
        UPLOAD PAGE JAVASCRIPT
=========================================*/
// ===================================
// Elements
// ===================================
let selectedFile = null;
const dropArea = document.getElementById("dropArea");
const fileInput = document.getElementById("fileInput");
const previewCard = document.getElementById("previewCard");
const previewImage = document.getElementById("previewImage");
const progressContainer = document.getElementById("progressContainer");
const progressBar = document.getElementById("progressBar");
const removeBtn = document.getElementById("removeBtn");
// ===================================
// Browse File
// ===================================
fileInput.addEventListener("change", function () {
    if (this.files.length > 0) {
        uploadFile(this.files[0]);
    }
});
// ===================================
// Drag Events
// ===================================
["dragenter", "dragover"].forEach(eventName => {
    dropArea.addEventListener(eventName, function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropArea.style.background = "#eaf4ff";
        dropArea.style.borderColor = "#0d6efd";
    });
});
["dragleave", "drop"].forEach(eventName => {
    dropArea.addEventListener(eventName, function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropArea.style.background = "";
        dropArea.style.borderColor = "";
    });
});
// ===================================
// Drop File
// ===================================
dropArea.addEventListener("drop", function (e) {
    const file = e.dataTransfer.files[0];
    if (file) {
        uploadFile(file);
    }
});
// ===================================
// Upload Function
// ===================================
function uploadFile(file) {
    // Check Image
    if (!file.type.startsWith("image/")) {
        alert("Please upload an image file.");
        return;
    }
    selectedFile = file;
    progressContainer.classList.remove("d-none");
    let progress = 0;
    const interval = setInterval(() => {
        progress += 5;
        progressBar.style.width = progress + "%";
        progressBar.innerHTML = progress + "%";
        if (progress >= 100) {
            clearInterval(interval);
            showPreview(file);
        }
    }, 60);
}
// ===================================
// Show Preview
// ===================================
function showPreview(file) {
    const reader = new FileReader();
    reader.onload = function (e) {
        previewImage.src = e.target.result;
        previewCard.classList.remove("d-none");
    }
    reader.readAsDataURL(file);
}
// part -2
// ===================================
// Remove Uploaded Image
// ===================================
removeBtn.addEventListener("click", function () {
    fileInput.value = "";
    previewImage.src = "";
    previewCard.classList.add("d-none");
    progressContainer.classList.add("d-none");
    progressBar.style.width = "0%";
    progressBar.innerHTML = "0%";
    Swal.fire({
        icon: "success",
        title: "Removed",
        text: "Uploaded image removed successfully.",
        timer: 1500,
        showConfirmButton: false
    });
});
// ===================================
// AI Analyze Button
// ===================================
const analyzeBtn = document.getElementById("analyzeBtn");
analyzeBtn.addEventListener("click",async function () {
    if (previewImage.src === "") {
        Swal.fire({
            icon: "warning",
            title: "No Scan Uploaded",
            text: "Please upload a medical scan first."
        });
        return;
    }
    const patientName = document.getElementById("patientName").value;
    const age = document.getElementById("patientAge").value;
    const gender = document.getElementById("patientGender").value;
    const scanType = document.getElementById("scanType").value;


    const token = localStorage.getItem("access");

    if (!token) {
        Swal.fire({
            icon: "error",
            title: "Login Required"
        });
        return;
    }

    try {

        // Step 1 : Create Patient

        const patientResponse = await fetch(
            "http://127.0.0.1:8000/api/patients/",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json",

                    Authorization:
                        `Bearer ${token}`
                },

                body: JSON.stringify({

                    name:
                        document.getElementById("patientName").value,

                    age:
                        document.getElementById("patientAge").value,

                    gender:
                        document.getElementById("patientGender").value

                })

            }
        );

        const patient = await patientResponse.json();
        
        if (!patientResponse.ok) {
            Swal.fire({
                icon: "error",
                title: "Patient Creation Failed"
            });
            return;
        }
        // Step 2 : Create Report

        const formData = new FormData();

        formData.append("patient", patient.id);

        formData.append(
            "scan_type",
            document.getElementById("scanType").value
        );

        formData.append(
            "image",
            selectedFile
        );

        const reportResponse = await fetch(
            "http://127.0.0.1:8000/api/reports/",
            {

                method: "POST",

                headers: {

                    Authorization:
                        `Bearer ${token}`

                },

                body: formData

            });
         

        const report = await reportResponse.json();
        if (!reportResponse.ok) {
            Swal.fire({
                icon: "error",
                title: "Report Generation Failed",
                text: report.recommendation || "Unknown Error"
            });
            return;
        }
        localStorage.setItem("lastReportId", report.id);
        Swal.fire({

            icon: "success",

            title: "AI Analysis Completed",

            html: `
            <b>Prediction:</b> ${report.ai_prediction}<br>
            <b>Confidence:</b> ${report.confidence}%<br>
            <b>Status:</b> ${report.status}
            `

        });
        setTimeout(() => {
            window.location.href = "/reports/";
        }, 1500);

    }
    catch (error) {

        console.log(error);

        Swal.fire({

            icon: "error",

            title: "Upload Failed"

        });

    }
});
// ===================================
// Drag Area Click Support
// ===================================
dropArea.addEventListener("click", function(){
    fileInput.click();
});
// ===================================
// File Name Display
// ===================================
fileInput.addEventListener("change", function(){
    if(this.files.length>0){
        Swal.fire({
            icon:"success",
            title:"File Selected",
            text:this.files[0].name,
            timer:1500,
            showConfirmButton:false
        });
    }
});