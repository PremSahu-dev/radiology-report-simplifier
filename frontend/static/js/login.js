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

    form.addEventListener("submit", async function (e) {
        

        e.preventDefault();

        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();

        if (username === "" || password === "") {

            Swal.fire({
                icon: "warning",
                title: "Missing Fields",
                text: "Please enter username and password."
            });

            return;
        }

        try {

            const response = await fetch("http://127.0.0.1:8000/api/accounts/login/", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    username: username,
                    password: password
                })

            });

            const data = await response.json();
            console.log("Login response:", data);
            
            if (response.ok) {

                localStorage.setItem("access", data.access);
                localStorage.setItem("refresh", data.refresh);
                localStorage.setItem("username", username);


                console.log("Access Token:", localStorage.getItem("access"));
                console.log("Refresh Token:", localStorage.getItem("refresh"));
                console.log(localStorage.getItem("access"));
                Swal.fire({
                    icon: "success",
                    title: "Login Successful",
                    timer: 1500,
                    showConfirmButton: false
                });

                setTimeout(() => {

                    window.location.href = "/dashboard/";

                }, 1500);

            } else {

                Swal.fire({
                    icon: "error",
                    title: "Login Failed",
                    text: data.non_field_errors
                        ? data.non_field_errors[0]
                        : "Invalid username or password."
                });

            }

        }

        catch (error) {

            Swal.fire({
                icon: "error",
                title: "Server Error",
                text: "Could not connect to Django backend."
            });

            console.log(error);

        }

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
