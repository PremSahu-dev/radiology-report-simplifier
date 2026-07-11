/*=========================================
        SETTINGS PAGE JAVASCRIPT
=========================================*/
<<<<<<< HEAD
// ================================
// Page Load Animation
// ================================
window.addEventListener("load", function () {
    const cards = document.querySelectorAll(".settings-card");
    cards.forEach((card, index) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(25px)";
        setTimeout(() => {
            card.style.transition = "0.6s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 150);
    });
});
// ================================
// Theme Selection
// ================================
const themeSelect = document.getElementById("themeSelect");
if (themeSelect) {
    // Load saved theme
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        themeSelect.value = savedTheme;
        if (savedTheme === "dark") {
            document.body.classList.add("dark-mode");
        }
    }
    themeSelect.addEventListener("change", function () {
        const selectedTheme = this.value;
        localStorage.setItem("theme", selectedTheme);
        if (selectedTheme === "dark") {
            document.body.classList.add("dark-mode");
        } else {
            document.body.classList.remove("dark-mode");
        }
        Swal.fire({
            icon: "success",
            title: "Theme Updated",
            text: `Theme changed to ${selectedTheme}.`,
            timer: 1500,
            showConfirmButton: false
        });
    });
}
// ================================
// Language Selection
// ================================
const languageSelect = document.getElementById("languageSelect");
if (languageSelect) {
    languageSelect.addEventListener("change", function () {
        Swal.fire({
            icon: "info",
            title: "Language Changed",
            text: `Selected Language: ${this.options[this.selectedIndex].text}`,
            timer: 1800,
            showConfirmButton: false
        });
    });
}
// ================================
// Compact Mode
// ================================
const compactMode = document.getElementById("compactMode");
if (compactMode) {
    compactMode.addEventListener("change", function () {
        document.body.classList.toggle("compact-layout");
        Swal.fire({
            toast: true,
            position: "top-end",
            icon: "success",
            title: this.checked ? "Compact Mode Enabled" : "Compact Mode Disabled",
            timer: 1800,
            showConfirmButton: false
        });
    });
}
=======

// ================================
// Page Load Animation
// ================================

window.addEventListener("load", function () {

    const cards = document.querySelectorAll(".settings-card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";
        card.style.transform = "translateY(25px)";

        setTimeout(() => {

            card.style.transition = "0.6s ease";

            card.style.opacity = "1";
            card.style.transform = "translateY(0)";

        }, index * 150);

    });

});

// ================================
// Theme Selection
// ================================

const themeSelect = document.getElementById("themeSelect");

if (themeSelect) {

    // Load saved theme

    const savedTheme = localStorage.getItem("theme");

    if (savedTheme) {

        themeSelect.value = savedTheme;

        if (savedTheme === "dark") {

            document.body.classList.add("dark-mode");

        }

    }

    themeSelect.addEventListener("change", function () {

        const selectedTheme = this.value;

        localStorage.setItem("theme", selectedTheme);

        if (selectedTheme === "dark") {

            document.body.classList.add("dark-mode");

        } else {

            document.body.classList.remove("dark-mode");

        }

        Swal.fire({

            icon: "success",

            title: "Theme Updated",

            text: `Theme changed to ${selectedTheme}.`,

            timer: 1500,

            showConfirmButton: false

        });

    });

}

// ================================
// Language Selection
// ================================

const languageSelect = document.getElementById("languageSelect");

if (languageSelect) {

    languageSelect.addEventListener("change", function () {

        Swal.fire({

            icon: "info",

            title: "Language Changed",

            text: `Selected Language: ${this.options[this.selectedIndex].text}`,

            timer: 1800,

            showConfirmButton: false

        });

    });

}

// ================================
// Compact Mode
// ================================

const compactMode = document.getElementById("compactMode");

if (compactMode) {

    compactMode.addEventListener("change", function () {

        document.body.classList.toggle("compact-layout");

        Swal.fire({

            toast: true,

            position: "top-end",

            icon: "success",

            title: this.checked ? "Compact Mode Enabled" : "Compact Mode Disabled",

            timer: 1800,

            showConfirmButton: false

        });

    });

}

>>>>>>> b56bf1d85936dbdc0aa9b0f260a884ea4f178117
<!-- part -2 -->
 // ================================
// Notification Settings
// ================================
<<<<<<< HEAD
const notificationToggles = document.querySelectorAll(
    "#emailNotification, #smsNotification, #pushNotification"
);
notificationToggles.forEach(toggle => {
    toggle.addEventListener("change", function () {
        const label = document.querySelector(`label[for="${this.id}"]`);
        Swal.fire({
            toast: true,
            position: "top-end",
            icon: "success",
            title: `${label.textContent.trim()} ${this.checked ? "Enabled" : "Disabled"}`,
            timer: 1800,
            showConfirmButton: false,
            timerProgressBar: true
        });
    });
});
// ================================
// Privacy & Security
// ================================
const securityToggles = document.querySelectorAll(
    "#twoFactor, #loginAlert, #rememberDevice"
);
securityToggles.forEach(toggle => {
    toggle.addEventListener("change", function () {
        const label = document.querySelector(`label[for="${this.id}"]`);
        Swal.fire({
            toast: true,
            position: "top-end",
            icon: "success",
            title: `${label.textContent.trim()} ${this.checked ? "Enabled" : "Disabled"}`,
            timer: 1800,
            showConfirmButton: false,
            timerProgressBar: true
        });
    });
});
// ================================
// Remove Connected Device
// ================================
const removeButtons = document.querySelectorAll(".btn-outline-danger");
removeButtons.forEach(button => {
    button.addEventListener("click", function () {
        const device = this.closest(".setting-item");
        Swal.fire({
            title: "Remove Device?",
            text: "This device will be signed out.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Yes, Remove",
            cancelButtonText: "Cancel"
        }).then((result) => {
            if (result.isConfirmed) {
                device.remove();
                Swal.fire({
                    icon: "success",
                    title: "Device Removed",
                    text: "The selected device has been removed.",
                    timer: 1500,
                    showConfirmButton: false
                });
            }
        });
    });
});
// ================================
// Save Settings
// ================================
const saveSettings = document.getElementById("saveSettings");
if (saveSettings) {
    saveSettings.addEventListener("click", function () {
        Swal.fire({
            icon: "success",
            title: "Settings Saved",
            text: "Your preferences have been saved successfully.",
            timer: 1800,
            showConfirmButton: false
        });
    });
}
// ================================
// Reset Settings
// ================================
const resetSettings = document.getElementById("resetSettings");
if (resetSettings) {
    resetSettings.addEventListener("click", function () {
        Swal.fire({
            title: "Reset Settings?",
            text: "All settings will return to their default values.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Yes, Reset",
            cancelButtonText: "Cancel"
        }).then((result) => {
            if (result.isConfirmed) {
                document.querySelectorAll("input[type='checkbox']")
                    .forEach(input => {
                        input.checked = false;
                    });
                if (themeSelect) {
                    themeSelect.value = "light";
                    document.body.classList.remove("dark-mode");
                }
                if (languageSelect) {
                    languageSelect.value = "en";
                }
                localStorage.removeItem("theme");
                Swal.fire({
                    icon: "success",
                    title: "Settings Reset",
                    text: "Default settings have been restored.",
                    timer: 1800,
                    showConfirmButton: false
                });
            }
        });
    });
}
<!-- part -3 -->
// ================================
// Auto Save Toggle Preferences
// ================================
const allToggles = document.querySelectorAll(".form-check-input");
allToggles.forEach(toggle => {
    // Load saved value
    const savedValue = localStorage.getItem(toggle.id);
    if (savedValue !== null) {
        toggle.checked = savedValue === "true";
    }
    // Save on change
    toggle.addEventListener("change", function () {
        localStorage.setItem(this.id, this.checked);
    });
});
// ================================
// Auto Save Language
// ================================
if (languageSelect) {
    const savedLanguage = localStorage.getItem("language");
    if (savedLanguage) {
        languageSelect.value = savedLanguage;
    }
    languageSelect.addEventListener("change", function () {
        localStorage.setItem("language", this.value);
    });
}
// ================================
// Welcome Toast
// ================================
setTimeout(() => {
    Swal.fire({
        toast: true,
        position: "top-end",
        icon: "success",
        title: "Settings Loaded Successfully",
        showConfirmButton: false,
        timer: 2000,
        timerProgressBar: true
    });
}, 800);
// ================================
// Smooth Card Hover Animation
// ================================
const cards = document.querySelectorAll(".settings-card");
cards.forEach(card => {
    card.addEventListener("mouseenter", function () {
        this.style.transform = "translateY(-5px) scale(1.01)";
    });
    card.addEventListener("mouseleave", function () {
        this.style.transform = "translateY(0) scale(1)";
    });
});
// ================================
// Future Backend Integration
// ================================
=======

const notificationToggles = document.querySelectorAll(
    "#emailNotification, #smsNotification, #pushNotification"
);

notificationToggles.forEach(toggle => {

    toggle.addEventListener("change", function () {

        const label = document.querySelector(`label[for="${this.id}"]`);

        Swal.fire({

            toast: true,

            position: "top-end",

            icon: "success",

            title: `${label.textContent.trim()} ${this.checked ? "Enabled" : "Disabled"}`,

            timer: 1800,

            showConfirmButton: false,

            timerProgressBar: true

        });

    });

});

// ================================
// Privacy & Security
// ================================

const securityToggles = document.querySelectorAll(
    "#twoFactor, #loginAlert, #rememberDevice"
);

securityToggles.forEach(toggle => {

    toggle.addEventListener("change", function () {

        const label = document.querySelector(`label[for="${this.id}"]`);

        Swal.fire({

            toast: true,

            position: "top-end",

            icon: "success",

            title: `${label.textContent.trim()} ${this.checked ? "Enabled" : "Disabled"}`,

            timer: 1800,

            showConfirmButton: false,

            timerProgressBar: true

        });

    });

});

// ================================
// Remove Connected Device
// ================================

const removeButtons = document.querySelectorAll(".btn-outline-danger");

removeButtons.forEach(button => {

    button.addEventListener("click", function () {

        const device = this.closest(".setting-item");

        Swal.fire({

            title: "Remove Device?",

            text: "This device will be signed out.",

            icon: "warning",

            showCancelButton: true,

            confirmButtonText: "Yes, Remove",

            cancelButtonText: "Cancel"

        }).then((result) => {

            if (result.isConfirmed) {

                device.remove();

                Swal.fire({

                    icon: "success",

                    title: "Device Removed",

                    text: "The selected device has been removed.",

                    timer: 1500,

                    showConfirmButton: false

                });

            }

        });

    });

});

// ================================
// Save Settings
// ================================

const saveSettings = document.getElementById("saveSettings");

if (saveSettings) {

    saveSettings.addEventListener("click", function () {

        Swal.fire({

            icon: "success",

            title: "Settings Saved",

            text: "Your preferences have been saved successfully.",

            timer: 1800,

            showConfirmButton: false

        });

    });

}

// ================================
// Reset Settings
// ================================

const resetSettings = document.getElementById("resetSettings");

if (resetSettings) {

    resetSettings.addEventListener("click", function () {

        Swal.fire({

            title: "Reset Settings?",

            text: "All settings will return to their default values.",

            icon: "warning",

            showCancelButton: true,

            confirmButtonText: "Yes, Reset",

            cancelButtonText: "Cancel"

        }).then((result) => {

            if (result.isConfirmed) {

                document.querySelectorAll("input[type='checkbox']")
                    .forEach(input => {

                        input.checked = false;

                    });

                if (themeSelect) {

                    themeSelect.value = "light";

                    document.body.classList.remove("dark-mode");

                }

                if (languageSelect) {

                    languageSelect.value = "en";

                }

                localStorage.removeItem("theme");

                Swal.fire({

                    icon: "success",

                    title: "Settings Reset",

                    text: "Default settings have been restored.",

                    timer: 1800,

                    showConfirmButton: false

                });

            }

        });

    });

}

<!-- part -3 -->

// ================================
// Auto Save Toggle Preferences
// ================================

const allToggles = document.querySelectorAll(".form-check-input");

allToggles.forEach(toggle => {

    // Load saved value
    const savedValue = localStorage.getItem(toggle.id);

    if (savedValue !== null) {

        toggle.checked = savedValue === "true";

    }

    // Save on change
    toggle.addEventListener("change", function () {

        localStorage.setItem(this.id, this.checked);

    });

});

// ================================
// Auto Save Language
// ================================

if (languageSelect) {

    const savedLanguage = localStorage.getItem("language");

    if (savedLanguage) {

        languageSelect.value = savedLanguage;

    }

    languageSelect.addEventListener("change", function () {

        localStorage.setItem("language", this.value);

    });

}

// ================================
// Welcome Toast
// ================================

setTimeout(() => {

    Swal.fire({

        toast: true,

        position: "top-end",

        icon: "success",

        title: "Settings Loaded Successfully",

        showConfirmButton: false,

        timer: 2000,

        timerProgressBar: true

    });

}, 800);

// ================================
// Smooth Card Hover Animation
// ================================

const cards = document.querySelectorAll(".settings-card");

cards.forEach(card => {

    card.addEventListener("mouseenter", function () {

        this.style.transform = "translateY(-5px) scale(1.01)";

    });

    card.addEventListener("mouseleave", function () {

        this.style.transform = "translateY(0) scale(1)";

    });

});

// ================================
// Future Backend Integration
// ================================

>>>>>>> b56bf1d85936dbdc0aa9b0f260a884ea4f178117
console.log("=================================");
console.log("MediScan AI Settings Module");
console.log("Status : Ready for Django Backend");
console.log("=================================");