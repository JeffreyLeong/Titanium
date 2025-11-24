document.addEventListener("DOMContentLoaded", function () {
  // Attach confirm to all forms that have class delete-form
  document.querySelectorAll("form.delete-form").forEach(form => {
    form.addEventListener("submit", function (e) {
      const ok = confirm("Are you sure you want to delete this record?");
      if (!ok) {
        e.preventDefault();
      }
    });
  });
});
