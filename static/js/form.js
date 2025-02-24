document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("search-form");
    const submitButton = document.getElementById("submit-button");

    form.addEventListener("submit", function () {
        submitButton.disabled = true;
        submitButton.value = 'Loading...';
        submitButton.setAttribute("aria-busy", "true");
        return true;
    });
});
