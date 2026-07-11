/*=========================================
        LOGIN PAGE JAVASCRIPT
=========================================*/
// ================================
// Show / Hide Password
// ================================
const password = document.getElementById("password");
const togglePassword = document.getElementById("togglePassword");
if (togglePassword && password) {
    togglePassword.addEventListener("click", function () {
        if (password.type === "password") {
            password.type = "text";
            this.classList.remove("fa-eye");
            this.classList.add("fa-eye-slash");
        } else {
            password.type = "password";
            this.classList.remove("fa-eye-slash");
            this.classList.add("fa-eye");
        }
    });
}
// ================================
// Input Focus Animation
// ================================
const inputs = document.querySelectorAll(".form-control");
inputs.forEach(input => {
    input.addEventListener("focus", function () {
        this.style.transition = "0.3s";
        this.style.transform = "scale(1.02)";
    });
    input.addEventListener("blur", function () {
        this.style.transform = "scale(1)";
    });
});
// ================================
// Login Button Animation
// ================================
const loginBtn = document.querySelector(".btn-primary");
if (loginBtn) {
    loginBtn.addEventListener("mouseenter", function () {
        this.style.transform = "translateY(-3px)";
    });
    loginBtn.addEventListener("mouseleave", function () {
        this.style.transform = "translateY(0px)";
    });
}
// changing part
// ================================
// Premium Login with SweetAlert
// ================================
const form = document.querySelector("form");
if (form) {
    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const email = document.querySelector('input[type="email"]').value.trim();
        const pass = document.getElementById("password").value.trim();
        if (email === "") {
            Swal.fire({
                icon: "warning",
                title: "Email Required",
                text: "Please enter your email address."
            });
            return;
        }
        if (!email.includes("@")) {
            Swal.fire({
                icon: "error",
                title: "Invalid Email",
                text: "Please enter a valid email address."
            });
            return;
        }
        if (pass.length < 8) {
            Swal.fire({
                icon: "error",
                title: "Weak Password",
                text: "Password must be at least 8 characters."
            });
            return;
        }
        const remember = document.getElementById("remember");
if (!remember.checked) {
    Swal.fire({
        icon: "warning",
        title: "Remember Me",
        text: "Please check Remember Me."
    });
    return;
}
        Swal.fire({
            title: "Checking Credentials...",
            html: "Connecting AI Server...",
            timer: 2500,
            allowOutsideClick: false,
            didOpen: () => {
                Swal.showLoading();
            }
        }).then(() => {
            Swal.fire({
                icon: "success",
                title: "Login Successful!",
                text: "Welcome to MediScan AI",
                timer: 1500,
                showConfirmButton: false
            }).then(() => {
                window.location.href = "dashboard.html";
            });
        });
    });
}
// change part ending
// // ================================
// Page Load Animation
// ================================
window.addEventListener("load", function () {
    const card = document.querySelector(".login-card");
    if (card) {
        card.style.opacity = "0";
        card.style.transform = "translateY(40px)";
        setTimeout(() => {
            card.style.transition = "0.7s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, 200);
    }
});
