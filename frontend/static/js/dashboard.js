// part -1

/*=========================================
        DASHBOARD JS
=========================================*/

document.addEventListener("DOMContentLoaded", function () {

    /*=====================================
            SIDEBAR TOGGLE
    =====================================*/

    const menuBtn = document.querySelector(".menu-btn");
    const sidebar = document.querySelector(".sidebar");

    if (menuBtn && sidebar) {

        menuBtn.addEventListener("click", () => {

            sidebar.classList.toggle("active");

        });

    }

    /*=====================================
            ACTIVE MENU
    =====================================*/

    const menuLinks = document.querySelectorAll(".menu li");

    menuLinks.forEach((item) => {

        item.addEventListener("click", function () {

            menuLinks.forEach((link) => {

                link.classList.remove("active");

            });

            this.classList.add("active");

        });

    });

    /*=====================================
            SEARCH FILTER
    =====================================*/

    const searchInput = document.querySelector(".search-box input");

    if (searchInput) {

        searchInput.addEventListener("keyup", function () {

            let value = this.value.toLowerCase();

            menuLinks.forEach((item) => {

                let text = item.innerText.toLowerCase();

                if (text.includes(value)) {

                    item.style.display = "block";

                } else {

                    item.style.display = "none";

                }

            });

        });

    }

    /*=====================================
            DARK MODE
    =====================================*/

    const darkBtn = document.querySelector(".dark-mode-btn");

    if (darkBtn) {

        darkBtn.addEventListener("click", () => {

            document.body.classList.toggle("dark-mode");

        });

    }

    /*=====================================
            COUNTER ANIMATION
    =====================================*/

    const counters = document.querySelectorAll(".card-info h2");

    counters.forEach(counter => {

        const updateCounter = () => {

            const target = +counter.innerText.replace(/\D/g, "");

            let count = +counter.getAttribute("data-count") || 0;

            const increment = Math.ceil(target / 50);

            if (count < target) {

                count += increment;

                counter.innerText = count;

                counter.setAttribute("data-count", count);

                setTimeout(updateCounter, 20);

            } else {

                counter.innerText = target;

            }

        };

        updateCounter();

    });

    /*=====================================
            WELCOME MESSAGE
    =====================================*/

    setTimeout(() => {

        console.log("Welcome to MediScan AI Dashboard 🚀");

    }, 1000);

});

// part -2

/*=========================================
        CHART.JS
=========================================*/

const chartCanvas = document.getElementById("analysisChart");

if (chartCanvas) {

    new Chart(chartCanvas, {

        type: "line",

        data: {

            labels: [

                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul"

            ],

            datasets: [

                {

                    label: "AI Reports",

                    data: [120,180,150,260,300,420,520],

                    borderColor: "#2563eb",

                    backgroundColor: "rgba(37,99,235,.15)",

                    fill: true,

                    borderWidth: 3,

                    tension: .4,

                    pointRadius: 5,

                    pointBackgroundColor: "#2563eb"

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: true

                }

            },

            scales: {

                y: {

                    beginAtZero: true

                }

            }

        }

    });

}

/*=========================================
        NOTIFICATION
=========================================*/

const notification = document.querySelector(".notification");

if(notification){

    notification.addEventListener("click",()=>{

        alert("🔔 No new notifications.");

    });

}

/*=========================================
        PROFILE
=========================================*/

const profile = document.querySelector(".profile");

if(profile){

    profile.addEventListener("click",()=>{

        alert("👤 Profile page will be available in Version 2.");

    });

}

/*=========================================
        UPLOAD BUTTON
=========================================*/

const uploadBtn = document.querySelector(".upload-area button");

if(uploadBtn){

    uploadBtn.addEventListener("click",()=>{

        alert("📤 Upload functionality will be connected with Django Backend.");

    });

}

/*=========================================
        LIVE CLOCK
=========================================*/

function updateTime(){

    const timeElement=document.getElementById("liveTime");

    if(timeElement){

        const now=new Date();

        timeElement.innerHTML=now.toLocaleTimeString();

    }

}

setInterval(updateTime,1000);

updateTime();

/*=========================================
        AI STATUS
=========================================*/

const aiStatus=document.querySelector(".text-success");

if(aiStatus){

    setInterval(()=>{

        aiStatus.style.opacity="0.5";

        setTimeout(()=>{

            aiStatus.style.opacity="1";

        },500);

    },1000);

}

/*=========================================
        SCROLL ANIMATION
=========================================*/

const cards=document.querySelectorAll(

".stats-card,.upload-card,.activity-card,.analytics-card,.profile-card,.tips-card,.report-card"

);

window.addEventListener("scroll",()=>{

    cards.forEach(card=>{

        const top=card.getBoundingClientRect().top;

        const windowHeight=window.innerHeight;

        if(top<windowHeight-100){

            card.style.opacity="1";

            card.style.transform="translateY(0)";

        }

    });

});

/*=========================================
        PAGE LOADED
=========================================*/

window.onload=function(){

    console.log("✅ MediScan AI Dashboard Loaded");

};

/*=========================================
        DEMO TOAST
=========================================*/

setTimeout(()=>{

    console.log("🤖 AI Engine Ready");

},2500);