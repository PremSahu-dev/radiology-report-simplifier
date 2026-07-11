/*=========================================
        FORGOT PASSWORD
=========================================*/

// ================================
// DOM Elements
// ================================

const email = document.getElementById("email");
const sendOtp = document.getElementById("sendOtp");
const otp = document.getElementById("otp");
const timer = document.getElementById("timer");
const resendOtp = document.getElementById("resendOtp");

// ================================
// Initial State
// ================================

let countdown;
let timeLeft = 60;

otp.disabled = true;
resendOtp.style.pointerEvents = "none";
resendOtp.style.opacity = "0.5";

// ================================
// Email Validation
// ================================

function validateEmail(emailValue){

    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    return pattern.test(emailValue);

}

// ================================
// Send OTP
// ================================

sendOtp.addEventListener("click", function(){

    const emailValue = email.value.trim();

    if(emailValue === ""){

        Swal.fire({

            icon:"warning",
            title:"Email Required",
            text:"Please enter your registered email."

        });

        return;

    }

    if(!validateEmail(emailValue)){

        Swal.fire({

            icon:"error",
            title:"Invalid Email",
            text:"Please enter a valid email address."

        });

        return;

    }

    Swal.fire({

        icon:"success",
        title:"OTP Sent",
        text:"A 6-digit OTP has been sent to your email. (Demo)",

        timer:1800,

        showConfirmButton:false

    });

    otp.disabled = false;

    sendOtp.disabled = true;

    startTimer();

});


// ==========================================
  // OTP VERIFICATION LOGIC (LOCAL 6-DIGIT CHECK)
  // ==========================================
  document.getElementById("verifyOtp").addEventListener("click", function () {
    let otpInput = document.getElementById("otp");

    if (!otpInput) {
      console.error("OTP input field missing in UI! Make sure <input id='otp'> exists.");
      return;
    }

    let otp = otpInput.value.trim();

    // Condition: Check agar input srf 6 numbers ka hai
    let is6Digit = /^\d{6}$/.test(otp); 

    if (!is6Digit) {
      Swal.fire({ 
        icon: "error", 
        title: "Invalid OTP", 
        text: "Please enter a valid 6-digit numeric OTP for testing!" 
      });
      return;
    }

    // --- MOCK SUCCESS (Bypassing Server for now) ---
    Swal.fire({
      icon: "success",
      title: "Testing Mode: OTP Verified!",
      showConfirmButton: false,
      timer: 1200
    });

    // OTP Section hide karo aur Password Section open karo
    document.getElementById("otpSection").style.display = "none";
    document.getElementById("passwordSection").style.display = "block";
    
    /* 
    // REAL PRODUCTION CODE (Baad me use karne ke liye comment kiya hai):
    let email = document.getElementById("email").value.trim();
    fetch("/verify-otp", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email, otp: otp }),
    })
    .then(res => res.json())
    .then(data => { ... })
    */
  });

  // ==========================================
  // NEW PASSWORD SUBMIT LOGIC
  // ==========================================
  document.getElementById("submitNewPassword").addEventListener("click", function() {
    let newPass = document.getElementById("newPassword").value;
    let confirmPass = document.getElementById("confirmPassword").value;

    if (newPass === "" || confirmPass === "") {
      Swal.fire({ icon: "warning", title: "Required", text: "Please fill both password fields!" });
      return;
    }

    if (newPass !== confirmPass) {
      Swal.fire({ icon: "error", title: "Mismatch", text: "Passwords do not match!" });
      return;
    }

    // For Testing: Bina server request ke success alert show karega
    Swal.fire({
      icon: "success",
      title: "Password Reset Done (Mock)!",
      text: "Testing successful! Moving to login page.",
      confirmButtonText: "Go to Login"
    }).then(() => {
      window.location.href = "login.html"; 
    });
  });


// ================================
// Countdown Timer
// ================================

function startTimer(){

    clearInterval(countdown);

    timeLeft = 60;

    timer.innerHTML = `OTP expires in ${timeLeft} seconds`;

    countdown = setInterval(function(){

        timeLeft--;

        timer.innerHTML = `OTP expires in ${timeLeft} seconds`;

        if(timeLeft <= 0){

            clearInterval(countdown);

            timer.innerHTML = "OTP Expired";

            resendOtp.style.pointerEvents = "auto";

            resendOtp.style.opacity = "1";

            sendOtp.disabled = false;

        }

    },1000);

}

// ================================
// Resend OTP
// ================================

resendOtp.addEventListener("click", function () {

    if (timeLeft > 0) return;

    Swal.fire({

        icon: "success",

        title: "OTP Resent",

        text: "A new OTP has been sent to your email. (Demo)",

        timer: 1800,

        showConfirmButton: false

    });

    resendOtp.style.pointerEvents = "none";

    resendOtp.style.opacity = "0.5";

    sendOtp.disabled = true;

    startTimer();

});

// ================================
// Show / Hide Password
// ================================

const togglePassword = document.querySelectorAll(".toggle-password");

togglePassword.forEach(button => {

    button.addEventListener("click", function () {

        const target = document.getElementById(
            this.getAttribute("data-target")
        );

        const icon = this.querySelector("i");

        if (target.type === "password") {

            target.type = "text";

            icon.classList.remove("fa-eye");

            icon.classList.add("fa-eye-slash");

        } else {

            target.type = "password";

            icon.classList.remove("fa-eye-slash");

            icon.classList.add("fa-eye");

        }

    });

});


// ================================
// Password Validation
// ================================

const newPassword = document.getElementById("newPassword");
const confirmPassword = document.getElementById("confirmPassword");

function validatePassword() {

    const password = newPassword.value.trim();

    const confirm = confirmPassword.value.trim();

    if (password.length < 8) {

        return {

            valid: false,

            message: "Password must contain at least 8 characters."

        };

    }

    if (password !== confirm) {

        return {

            valid: false,

            message: "Passwords do not match."

        };

    }

    return {

        valid: true,

        message: ""

    };

}

// ================================
// Live Validation
// ================================

confirmPassword.addEventListener("keyup", function () {

    if (this.value.length === 0) return;

    if (newPassword.value === this.value) {

        this.style.borderColor = "#198754";

    } else {

        this.style.borderColor = "#dc3545";

    }

});

// part -3
// ================================
// Reset Password
// ================================

const forgotForm = document.getElementById("forgotForm");

forgotForm.addEventListener("submit", function (e) {

    e.preventDefault();

    const emailValue = email.value.trim();
    const otpValue = otp.value.trim();

    // Email Check
    if (emailValue === "") {

        Swal.fire({
            icon: "warning",
            title: "Email Required",
            text: "Please enter your email."
        });

        return;
    }

    // OTP Check
    if (otpValue.length !== 6) {

        Swal.fire({
            icon: "error",
            title: "Invalid OTP",
            text: "Please enter a valid 6-digit OTP."
        });

        return;
    }

    // Password Check
    const result = validatePassword();

    if (!result.valid) {

        Swal.fire({
            icon: "error",
            title: "Password Error",
            text: result.message
        });

        return;
    }

    // Demo Save
    localStorage.setItem("userPassword", newPassword.value);

    Swal.fire({

        icon: "success",

        title: "Password Reset Successful",

        text: "Your password has been reset successfully.",

        confirmButtonText: "Go to Login"

    }).then(() => {

        window.location.href = "login.html";

    });

});

// ================================
// Prevent OTP Input > 6 Digits
// ================================

otp.addEventListener("input", function () {

    this.value = this.value.replace(/\D/g, "").slice(0, 6);

});

// ================================
// Auto Focus Password
// ================================

otp.addEventListener("keyup", function () {

    if (this.value.length === 6) {

        newPassword.focus();

    }

});

// ================================
// Console Message
// ================================

console.log("=================================");
console.log("MediScan AI Forgot Password Module");
console.log("Status : Frontend Complete");
console.log("Ready : Django Backend Integration");
console.log("=================================");

