// part -1
<<<<<<< HEAD
/*=========================================
        UPLOAD PAGE JAVASCRIPT
=========================================*/
// ===================================
// Elements
// ===================================
=======

/*=========================================
        UPLOAD PAGE JAVASCRIPT
=========================================*/

// ===================================
// Elements
// ===================================

>>>>>>> b56bf1d85936dbdc0aa9b0f260a884ea4f178117
const dropArea = document.getElementById("dropArea");
const fileInput = document.getElementById("fileInput");
const previewCard = document.getElementById("previewCard");
const previewImage = document.getElementById("previewImage");
const progressContainer = document.getElementById("progressContainer");
const progressBar = document.getElementById("progressBar");
const removeBtn = document.getElementById("removeBtn");
<<<<<<< HEAD
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
analyzeBtn.addEventListener("click", function () {
    if (previewImage.src === "") {
        Swal.fire({
            icon: "warning",
            title: "No Scan Uploaded",
            text: "Please upload a medical scan first."
        });
        return;
    }
    Swal.fire({
        title: "Analyzing Scan...",
        html: `
            <b>AI Model Loading...</b><br><br>
            <div class="progress">
                <div id="aiProgress"
                     class="progress-bar progress-bar-striped progress-bar-animated"
                     style="width:0%">
                    0%
                </div>
            </div>
        `,
        allowOutsideClick: false,
        showConfirmButton: false,
        didOpen: () => {
            let progress = 0;
            const bar = document.getElementById("aiProgress");
            const timer = setInterval(() => {
                progress += 5;
                bar.style.width = progress + "%";
                bar.innerHTML = progress + "%";
                if (progress >= 100) {
                    clearInterval(timer);
                    Swal.fire({
                        icon: "success",
                        title: "Analysis Complete",
                        text: "AI has successfully analyzed the scan.",
                        timer: 2000,
                        showConfirmButton: false
                    }).then(() => {
                        // Future Django Result Page
                         window.location.href="result.html";
                    });
                }
            },120);
        }
    });
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
=======

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

analyzeBtn.addEventListener("click", function () {

    if (previewImage.src === "") {

        Swal.fire({

            icon: "warning",

            title: "No Scan Uploaded",

            text: "Please upload a medical scan first."

        });

        return;

    }

    Swal.fire({

        title: "Analyzing Scan...",

        html: `

            <b>AI Model Loading...</b><br><br>

            <div class="progress">

                <div id="aiProgress"
                     class="progress-bar progress-bar-striped progress-bar-animated"
                     style="width:0%">

                    0%

                </div>

            </div>

        `,

        allowOutsideClick: false,

        showConfirmButton: false,

        didOpen: () => {

            let progress = 0;

            const bar = document.getElementById("aiProgress");

            const timer = setInterval(() => {

                progress += 5;

                bar.style.width = progress + "%";

                bar.innerHTML = progress + "%";

                if (progress >= 100) {

                    clearInterval(timer);

                    Swal.fire({

                        icon: "success",

                        title: "Analysis Complete",

                        text: "AI has successfully analyzed the scan.",

                        timer: 2000,

                        showConfirmButton: false

                    }).then(() => {

                        // Future Django Result Page

                         window.location.href="result.html";

                    });

                }

            },120);

        }

    });

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

>>>>>>> b56bf1d85936dbdc0aa9b0f260a884ea4f178117
});