/*=========================================
        RESULT PAGE JAVASCRIPT
=========================================*/
<<<<<<< HEAD
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
        Swal.fire({
=======

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

        Swal.fire({

>>>>>>> b56bf1d85936dbdc0aa9b0f260a884ea4f178117
            title: "Generating PDF...",
            text: "Please wait...",
            allowOutsideClick: false,
            didOpen: () => {
<<<<<<< HEAD
                Swal.showLoading();
            }
        });
        setTimeout(() => {
            Swal.fire({
                icon: "success",
                title: "PDF Ready",
                text: "Backend integration will enable real PDF download."
            });
        }, 2000);
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
=======

                Swal.showLoading();

            }

        });

        setTimeout(() => {

            Swal.fire({

                icon: "success",

                title: "PDF Ready",

                text: "Backend integration will enable real PDF download."

            });

        }, 2000);

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

>>>>>>> b56bf1d85936dbdc0aa9b0f260a884ea4f178117
}