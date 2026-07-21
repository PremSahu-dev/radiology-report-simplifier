// part - 1
/*=========================================
        REPORTS PAGE JAVASCRIPT
=========================================*/
// ================================
// Page Load Animation
// ================================
console.log("REPORTS JS LOADED");
alert("REPORTS JS LOADED");
window.addEventListener("load", function () {
    const cards = document.querySelectorAll(
        ".search-card, .table-card, .stats-card, .quick-actions"
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
// Search Reports
// ================================
const searchInput = document.getElementById("searchInput");
if (searchInput) {
    searchInput.addEventListener("keyup", function () {
        const value = this.value.toLowerCase();
        const rows = document.querySelectorAll("#reportTable tbody tr");
        rows.forEach(row => {
            row.style.display =
                row.innerText.toLowerCase().includes(value)
                    ? ""
                    : "none";
        });
    });
}
// ================================
// Status Filter
// ================================
const statusFilter = document.getElementById("statusFilter");
if (statusFilter) {
    statusFilter.addEventListener("change", function () {
        const value = this.value.toLowerCase();
        const rows = document.querySelectorAll("#reportTable tbody tr");
        // rows.forEach(row => {
        //     if (value === "all") {
        //         row.style.display = "";
        //         return;
        //     }
        //     const status = row.cells[6].innerText.toLowerCase();
        //     row.style.display = status.includes(value)
        //         ? ""
        //         : "none";
        // });
        rows.forEach(row => {

            if (value === "all") {
                row.style.display = "";
                return;
            }

            const status = row.cells[6].innerText.toLowerCase();

            row.style.display =
                status.includes(value)
                    ? ""
                    : "none";

        });
    });
}
// part - 2
// ================================
// Download Report
// ================================
const downloadButtons = document.querySelectorAll(".downloadBtn");
downloadButtons.forEach(button => {
    button.addEventListener("click", function () {
        Swal.fire({
            title: "Generating PDF...",
            text: "Please wait while your report is being prepared.",
            allowOutsideClick: false,
            didOpen: () => {
                Swal.showLoading();
            }
        });
        setTimeout(() => {
            Swal.fire({
                icon: "success",
                title: "Download Ready",
                text: "Demo Version: PDF download will be available after backend integration."
            });
        }, 2000);
    });
});
// ================================
// Delete Report
// ================================
const deleteButtons = document.querySelectorAll(".deleteBtn");
deleteButtons.forEach(button => {
    button.addEventListener("click", function () {
        const row = this.closest("tr");
        Swal.fire({
            title: "Delete Report?",
            text: "This action cannot be undone.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#dc3545",
            cancelButtonColor: "#6c757d",
            confirmButtonText: "Yes, Delete"
        }).then((result) => {
            if (result.isConfirmed) {
                row.remove();
                Swal.fire({
                    icon: "success",
                    title: "Deleted",
                    text: "Report deleted successfully."
                });
            }
        });
    });
});
// ================================
// View Report Animation
// ================================
const viewButtons = document.querySelectorAll('a[href="result.html"]');
viewButtons.forEach(button => {
    button.addEventListener("click", function () {
        Swal.fire({
            title: "Opening Report...",
            timer: 1000,
            showConfirmButton: false,
            didOpen: () => {
                Swal.showLoading();
            }
        });
    });
});
// part - 3
// ================================
// Download All Reports
// ================================
const downloadAll = document.getElementById("downloadAll");
if (downloadAll) {
    downloadAll.addEventListener("click", function () {
        Swal.fire({
            title: "Preparing Reports...",
            html: "Creating ZIP File...",
            allowOutsideClick: false,
            didOpen: () => {
                Swal.showLoading();
            }
        });
        setTimeout(() => {
            Swal.fire({
                icon: "success",
                title: "Download Ready!",
                text: "Backend integration will download all reports as ZIP."
            });
        }, 2500);
        
    });
}
// ================================
// Delete All Reports
// ================================
const deleteAll = document.getElementById("deleteAll");
if (deleteAll) {
    deleteAll.addEventListener("click", function () {
        Swal.fire({
            title: "Delete All Reports?",
            text: "This action cannot be undone.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#dc3545",
            cancelButtonColor: "#6c757d",
            confirmButtonText: "Yes, Delete All"
        }).then((result) => {
            if (result.isConfirmed) {
                document.querySelector("#reportTable tbody").innerHTML = "";
                updateStatistics();
                Swal.fire({
                    icon: "success",
                    title: "Deleted!",
                    text: "All reports have been deleted."
                });
            }
        });
    });
}
// ================================
// Auto Update Statistics
// ================================
function updateStatistics() {
    const rows = document.querySelectorAll("#reportTable tbody tr");
    let total = rows.length;
    let completed = 0;
    let pending = 0;
    rows.forEach(row => {

        if (row.cells.length < 7) return;

        const status = row.cells[6].innerText.trim();

        if (status === "Completed") {
            completed++;
        }

        if (status === "Pending") {
            pending++;
        }

    });
    
    const cards = document.querySelectorAll(".stats-content h3");
    if (cards.length >= 3) {
        cards[0].textContent = total;
        cards[1].textContent = completed;
        cards[2].textContent = pending;
    }
}
updateStatistics();
// ================================
// Last Updated Time
// ================================
const lastUpdated = document.getElementById("lastUpdated");
if (lastUpdated) {
    const now = new Date();
    lastUpdated.innerHTML = now.toLocaleString();
}
// ================================
// Welcome Notification
// ================================
setTimeout(() => {
    Swal.fire({
        toast: true,
        position: "top-end",
        icon: "success",
        title: "Reports Loaded Successfully",
        showConfirmButton: false,
        timer: 2500,
        timerProgressBar: true
    });
}, 800);

const token = localStorage.getItem("access");

if (token) {

    fetch("http://127.0.0.1:8000/api/reports/", {
        
        headers: {
            Authorization: `Bearer ${token}`
        }

    })
   

        // .then(res => {
        //     console.log("Status:", res.status);
        //     return res.json();
        // })
    //     .then(data => {
    //         console.log("Reports:", data);
    //         console.log("About to fetch reports...");

    //         const tbody = document.querySelector("#reportTable tbody");
    //         console.log("TBODY:", tbody);
    //         console.log("Length:", data.length);
    //         tbody.innerHTML = "";
    //         tbody.innerHTML = "<tr><td colspan='8'>TEST ROW</td></tr>";


    //         data.forEach(report => {
    //             console.log(report);
    //             tbody.innerHTML += `
    //     <tr>
    //         <td>${report.id}</td>
    //         <td>${report.patient_name}</td>
    //         <td>${report.scan_type}</td>
    //         <td>${report.ai_prediction}</td>
    //         <td>${report.confidence}</td>
    //         <td>${report.created_at.substring(0, 10)}</td>
    //         <td>${report.status}</td>
    //         <td>
    //        <button class="btn btn-primary btn-sm">
    //         View
    //        </button>
    // </td>
    //     </tr>
    //     `;
    //         });

    //         updateStatistics();
    //     })  



    //     .catch(error => {
    //         console.log(error);

    //         Swal.fire({
    //             icon: "error",
    //             title: "Failed to load reports"
    //         });
    //     });
        // .then(data => {

        //     console.log(data);

        //     const tbody = document.querySelector("#reportTable tbody");

        //     tbody.innerHTML = "";

        //     data.forEach(function (report) {

        //         console.log(report);

        //         const row = document.createElement("tr");

        //         row.innerHTML = `
        //     <td>${report.id}</td>
        //     <td>${report.patient_name}</td>
        //     <td>${report.scan_type}</td>
        //     <td>${report.ai_prediction}</td>
        //     <td>${report.confidence}</td>
        //     <td>${report.created_at}</td>
        //     <td>${report.status}</td>
        //     <td>
        //         <button class="btn btn-primary btn-sm">View</button>
        //     </td>
        // `;

        //         tbody.appendChild(row);

        //     });

        //     console.log("Rows:", tbody.rows.length);

        //     updateStatistics();

        // })
        .then(async res => {

            console.log("Status:", res.status);

            const data = await res.json();

            if (!res.ok) {
                console.log(data);

                Swal.fire({
                    icon: "error",
                    title: "Session Expired",
                    text: "Please login again."
                });

                localStorage.removeItem("access");
                localStorage.removeItem("refresh");

                window.location.href = "/login/";

                return;
            }

            return data;

        })
        .then(data => {

            if (!data) return;

            console.log(data);

            data.forEach(report => {

                // existing code

            });

        })

}