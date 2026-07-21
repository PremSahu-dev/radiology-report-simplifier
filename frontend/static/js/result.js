/*=========================================
        RESULT PAGE JAVASCRIPT
=========================================*/
// ================================
// Page Load Animation
// ================================
window.addEventListener("load", function () {
    const card = document.querySelector(".diagnosis-card");
    if (card) {
        card.style.opacity = "0";
        card.style.transform = "translateY(40px)";
        setTimeout(() => {
            card.style.transition = ".7s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, 200);
    }
});
// ================================
// Confidence Progress Animation
// ================================
const progressBar = document.querySelector(".progress-bar");
if (progressBar) {
    const target = 98;
    let value = 0;
    progressBar.style.width = "0%";
    progressBar.innerHTML = "0%";
    const interval = setInterval(() => {
        value++;
        progressBar.style.width = value + "%";
        progressBar.innerHTML = value + "%";
        if (value >= target) {
            clearInterval(interval);
        }
    }, 20);
}
// ================================
// Download PDF Button
// ================================
const downloadBtn = document.getElementById("downloadBtn");

if (downloadBtn) {

    downloadBtn.addEventListener("click", function () {
        const id = localStorage.getItem("lastReportId");

        const token = localStorage.getItem("access");

        fetch(
            "http://127.0.0.1:8000/api/reports/" + id + "/download_pdf/",
            {
                headers: {
                    Authorization: "Bearer " + token
                }
            }
        )
            .then(res => res.blob())
            .then(blob => {

                const url = window.URL.createObjectURL(blob);

                const a = document.createElement("a");

                a.href = url;

                a.download = "Medical_Report.pdf";

                a.click();

                window.URL.revokeObjectURL(url);

            });

    });
        

}
        
// ================================
// Email Button
// ================================
const emailBtn = document.getElementById("emailBtn");
if (emailBtn) {
    emailBtn.addEventListener("click", function () {
        Swal.fire({
            icon: "success",
            title: "Email Sent",
            text: "Report sent successfully (Demo Version)."
        });
    });
}
const printBtn = document.getElementById("printBtn");

if (printBtn) {

    printBtn.addEventListener("click", function () {

        const content =
            document.querySelector(".result-card").innerHTML;

        const w = window.open("", "", "width=900,height=700");

        w.document.write(`
       <html>
         <head>
         <title>Medical Report</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
       ${content}
      </body>
      </html>
     `);

        w.document.close();
        w.print();
        w.close();

    });

}

const id = localStorage.getItem("lastReportId");
const token = localStorage.getItem("access");

if (id && token) {

    fetch("http://127.0.0.1:8000/api/reports/" + id + "/", {

        headers: {
            Authorization: "Bearer " + token
        }

    })

        .then(res => res.json())

        .then(report => {

            document.getElementById("patientName").innerText =
                report.patient_name;

            document.getElementById("scanType").innerText =
                report.scan_type;

            document.getElementById("prediction").innerText =
                report.ai_prediction;

            document.getElementById("confidence").innerText =
                report.confidence + "%";

            document.getElementById("severity").innerText =
                report.severity;

            document.getElementById("recommendation").innerText =
                report.recommendation;

            document.getElementById("doctorNotes").innerText =
                "Reviewed by AI Engine";

            document.getElementById("reportDate").textContent =
                report.created_at.substring(0, 10);

        });

}