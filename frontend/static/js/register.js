/*=========================================
        REGISTER PAGE JAVASCRIPT
=========================================*/
//=========================================
// PASSWORD SHOW / HIDE
//=========================================
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");
const togglePassword = document.getElementById("togglePassword");
const toggleConfirm = document.getElementById("toggleConfirm");
if(togglePassword){
    togglePassword.addEventListener("click",function(){
        if(password.type==="password"){
            password.type="text";
            this.classList.remove("fa-eye");
            this.classList.add("fa-eye-slash");
        }
        else{
            password.type="password";
            this.classList.remove("fa-eye-slash");
            this.classList.add("fa-eye");
        }
    });
}
if(toggleConfirm){
    toggleConfirm.addEventListener("click",function(){
        if(confirmPassword.type==="password"){
            confirmPassword.type="text";
            this.classList.remove("fa-eye");
            this.classList.add("fa-eye-slash");
        }
        else{
            confirmPassword.type="password";
            this.classList.remove("fa-eye-slash");
            this.classList.add("fa-eye");
        }
    });
}
//=========================================
// PASSWORD STRENGTH
//=========================================
password.addEventListener("keyup",function(){
    const value=password.value;
    let strength="Weak";
    if(value.length>=8){
        strength="Medium";
    }
    if(
        value.length>=8 &&
        /[A-Z]/.test(value) &&
        /[a-z]/.test(value) &&
        /[0-9]/.test(value) &&
        /[^A-Za-z0-9]/.test(value)
    ){
        strength="Strong";
    }
    console.log("Password Strength :",strength);
});
//=========================================
// FORM VALIDATION
//=========================================
const form=document.getElementById("registerForm");
form.addEventListener("submit",function(e){
    e.preventDefault();
    const name=document.querySelector('input[type="text"]').value.trim();
    const email=document.querySelector('input[type="email"]').value.trim();
    const mobile=document.querySelector('input[type="tel"]').value.trim();
    const pass=password.value;
    const confirm=confirmPassword.value;
    const terms=document.getElementById("terms");
    // Name
    if(name===""){
        alert("Please enter your Full Name.");
        return;
    }
    // Email
    const emailPattern=/^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if(!email.match(emailPattern)){
        alert("Enter a valid Email Address.");
        return;
    }
    // Mobile
    if(mobile.length!=10 || isNaN(mobile)){
        alert("Enter a valid 10-digit Mobile Number.");
        return;
    }
    // Password Length
    if(pass.length<8){
        alert("Password must be at least 8 characters.");
        return;
    }
    // Password Match
    if(pass!==confirm){
        alert("Password and Confirm Password do not match.");
        return;
    }
    // Terms
    if(!terms.checked){
        alert("Please accept Terms & Conditions.");
        return;
    }
    alert("🎉 Account Created Successfully!");
});
//=========================================
// INPUT FOCUS EFFECT
//=========================================
const inputs=document.querySelectorAll(".form-control");
inputs.forEach(input=>{
    input.addEventListener("focus",function(){
        this.style.transform="scale(1.02)";
    });
    input.addEventListener("blur",function(){
        this.style.transform="scale(1)";
    });
});
//=========================================
// PAGE LOAD ANIMATION
//=========================================
window.addEventListener("load",function(){
    const card=document.querySelector(".register-card");
    card.style.opacity="0";
    card.style.transform="translateY(40px)";
    setTimeout(()=>{
        card.style.transition=".7s";
        card.style.opacity="1";
        card.style.transform="translateY(0px)";
    },200);
});