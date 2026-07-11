/*=========================================
        GLOBAL THEME MANAGER
=========================================*/
<<<<<<< HEAD
(function () {
    const savedTheme = localStorage.getItem("theme") || "light";
    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");
    } else {

        document.body.classList.remove("dark-mode");
    }
=======

(function () {

    const savedTheme = localStorage.getItem("theme") || "light";

    if (savedTheme === "dark") {

        document.body.classList.add("dark-mode");

    } else {

        document.body.classList.remove("dark-mode");

    }

>>>>>>> b56bf1d85936dbdc0aa9b0f260a884ea4f178117
})();