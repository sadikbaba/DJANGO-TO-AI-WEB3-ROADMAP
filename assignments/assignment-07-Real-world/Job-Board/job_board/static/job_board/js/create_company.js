const logoInput = document.getElementById("id_logo");
const logoPreview = document.getElementById("logo-preview");
const removeButton = document.getElementById("remove-logo");

logoInput.addEventListener("change", function () {
  const file = logoInput.files[0];

  if (!file) {
    return;
  }

  logoPreview.src = URL.createObjectURL(file);

  logoPreview.classList.add("show");
  removeButton.classList.add("show-remove");
});

removeButton.addEventListener("click", function () {
  logoInput.value = "";
  logoPreview.src = "";

  logoPreview.classList.remove("show");
  removeButton.classList.remove("show-remove");
});
