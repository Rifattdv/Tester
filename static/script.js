// Optional alerts for realism
const forms = document.querySelectorAll("form");
forms.forEach(form => {
    form.addEventListener("submit", () => {
        alert("Transaction submitted! Check dashboard for updates.");
    });
});
