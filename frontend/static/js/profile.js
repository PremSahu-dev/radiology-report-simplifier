/*=========================================
        PROFILE PAGE JAVASCRIPT
=========================================*/
// ================================
// Page Load Animation
// ================================
window.addEventListener("load", function () {
    const cards = document.querySelectorAll(
        ".profile-card, .security-card, .preferences-card, .account-stats, .activity-card"
    );
    cards.forEach((card, index) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(30px)";
        setTimeout(() => {
            card.style.transition = "0.6s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 150);
    });
});
// ================================
// Profile Image Upload
// ================================
const profileUpload = document.getElementById("profileUpload");
const profilePreview = document.getElementById("profilePreview");
const changePhoto = document.getElementById("changePhoto");
if (changePhoto && profileUpload && profilePreview) {
    changePhoto.addEventListener("click", function () {
        profileUpload.click();
    });
    profileUpload.addEventListener("change", function () {
        const file = this.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = function (e) {
            profilePreview.src = e.target.result;
            Swal.fire({
                icon: "success",
                title: "Profile Photo Updated",
                text: "Preview updated successfully.",
                timer: 1500,
                showConfirmButton: false
            });
        };
        reader.readAsDataURL(file);
    });
}
// ================================
// Input Focus Animation
// ================================
const inputs = document.querySelectorAll(
    ".form-control, .form-select"
);
inputs.forEach(input => {
    input.addEventListener("focus", function () {
        this.style.transform = "scale(1.02)";
    });
    input.addEventListener("blur", function () {
        this.style.transform = "scale(1)";
    });
});
// ================================
// Save Profile
// ================================
const profileForm = document.getElementById("profileForm");
if (profileForm) {
    profileForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const fullName = document
            .getElementById("fullName")
            .value.trim();
        const email = document
            .getElementById("email")
            .value.trim();
        if (fullName === "") {
            Swal.fire({
                icon: "warning",
                title: "Full Name Required",
                text: "Please enter your full name."
            });
            return;
        }
        if (!email.includes("@")) {
            Swal.fire({
                icon: "error",
                title: "Invalid Email",
                text: "Please enter a valid email."
            });
            return;
        }
        Swal.fire({
            icon: "success",
            title: "Profile Updated",
            text: "Your profile has been updated successfully.",
            timer: 1800,
            showConfirmButton: false
        });
    });
}
// part - 2
// ================================
// Show / Hide Password
// ================================
const togglePasswords = document.querySelectorAll(".toggle-password");
togglePasswords.forEach(toggle => {
    toggle.addEventListener("click", function () {
        const input = this.parentElement.querySelector("input");
        const icon = this.querySelector("i");
        if (input.type === "password") {
            input.type = "text";
            icon.classList.remove("fa-eye");
            icon.classList.add("fa-eye-slash");
        } else {
            input.type = "password";
            icon.classList.remove("fa-eye-slash");
            icon.classList.add("fa-eye");
        }
    });
});
// ================================
// Change Password Validation
// ================================
const passwordForm = document.getElementById("passwordForm");
if (passwordForm) {
    passwordForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const currentPassword =
            document.getElementById("currentPassword").value.trim();
        const newPassword =
            document.getElementById("newPassword").value.trim();
        const confirmPassword =
            document.getElementById("confirmPassword").value.trim();
        if (
            currentPassword === "" ||
            newPassword === "" ||
            confirmPassword === ""
        ) {
            Swal.fire({
                icon: "warning",
                title: "Missing Fields",
                text: "Please fill in all password fields."
            });
            return;
        }
        if (newPassword.length < 8) {
            Swal.fire({
                icon: "error",
                title: "Weak Password",
                text: "New password must be at least 8 characters."
            });
            return;
        }
        if (newPassword !== confirmPassword) {
            Swal.fire({
                icon: "error",
                title: "Password Mismatch",
                text: "New Password and Confirm Password do not match."
            });
            return;
        }
        Swal.fire({
            icon: "success",
            title: "Password Changed",
            text: "Your password has been updated successfully.",
            timer: 1800,
            showConfirmButton: false
        });
        passwordForm.reset();
    });
}
// ================================
// Preferences Toggle
// ================================
const switches = document.querySelectorAll(".form-check-input");
switches.forEach(toggle => {
    toggle.addEventListener("change", function () {
        const label =
            this.nextElementSibling.textContent.trim();
        Swal.fire({
            toast: true,
            position: "top-end",
            icon: "success",
            title: `${label} ${this.checked ? "Enabled" : "Disabled"}`,
            showConfirmButton: false,
            timer: 1800,
            timerProgressBar: true
        });
    });
});
// part - 3
// ================================
// Statistics Counter Animation
// ================================
const statNumbers = document.querySelectorAll(".stat-card h3");
function animateCounter(element, target) {
    let count = 0;
    const increment = Math.max(1, Math.ceil(target / 60));
    const timer = setInterval(() => {
        count += increment;
        if (count >= target) {
            element.textContent = target;
            clearInterval(timer);
        } else {
            element.textContent = count;
        }
    }, 25);
}
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const cards = document.querySelectorAll(".stat-card h3");
            cards.forEach(card => {
                const value = parseInt(card.textContent);
                animateCounter(card, value);
            });
            observer.disconnect();
        }
    });
});
if (statNumbers.length > 0) {
    observer.observe(statNumbers[0]);
}
// ================================
// Last Login Auto Update
// ================================
const lastLogin = document.getElementById("lastLogin");
if (lastLogin) {
    const now = new Date();
    lastLogin.textContent = now.toLocaleString();
}
// ================================
// Welcome Toast
// ================================
setTimeout(() => {
    Swal.fire({
        toast: true,
        position: "top-end",
        icon: "success",
        title: "Welcome to your Profile",
        showConfirmButton: false,
        timer: 2200,
        timerProgressBar: true
    });
}, 700);
// ================================
// Drag & Drop Profile Image
// ================================
if (profilePreview && profileUpload) {
    profilePreview.addEventListener("dragover", function (e) {
        e.preventDefault();
        this.style.opacity = "0.7";
    });
    profilePreview.addEventListener("dragleave", function () {
        this.style.opacity = "1";
    });
    profilePreview.addEventListener("drop", function (e) {
        e.preventDefault();
        this.style.opacity = "1";
        const file = e.dataTransfer.files[0];
        if (!file || !file.type.startsWith("image/")) {
            Swal.fire({
                icon: "error",
                title: "Invalid File",
                text: "Please drop a valid image."
            });
            return;
        }
        const reader = new FileReader();
        reader.onload = function (event) {
            profilePreview.src = event.target.result;
            Swal.fire({
                icon: "success",
                title: "Profile Photo Updated",
                text: "Image uploaded successfully."
            });
        };
        reader.readAsDataURL(file);
    });
}
// ================================
// Future Backend Ready
// ================================
console.log("Profile Module Loaded Successfully");
console.log("Ready for Django Backend Integration");