/*=========================================
        GLOBAL THEME MANAGER
=========================================*/
(function () {
    const savedTheme = localStorage.getItem("theme") || "light";
    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");
    } else {

        document.body.classList.remove("dark-mode");
    }
})();