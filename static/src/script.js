try {
  const profileImageDropzone = document.getElementById(
    "profile-image-dropzone"
  );
  const profileImageInput = document.getElementById("profile_image");
  const previewImage = document.getElementById("preview");

  profileImageDropzone.addEventListener("dragover", (e) => {
    e.preventDefault();
    profileImageDropzone.classList.add("bg-gray-200");
  });

  profileImageDropzone.addEventListener("dragleave", (e) => {
    e.preventDefault();
    profileImageDropzone.classList.remove("bg-gray-200");
  });

  profileImageDropzone.addEventListener("drop", (e) => {
    e.preventDefault();
    const droppedFiles = e.dataTransfer.files;

    // Basic validation (replace with your preferred logic)
    if (droppedFiles.length === 0) {
      alert("Please select an image file");
      return;
    }

    const acceptedExtensions = ["jpg", "jpeg", "png"];
    const fileExtension = droppedFiles[0].name.split(".").pop().toLowerCase();

    if (!acceptedExtensions.includes(fileExtension)) {
      alert("Only JPG, JPEG, and PNG files are allowed");
      return;
    }

    // Assuming you have logic to handle the uploaded file (e.g., sending to server)
    // ... your upload logic here ...

    // Update preview image (replace with your preferred method)
    const reader = new FileReader();
    reader.onload = function (e) {
      previewImage.src = e.target.result;
    };
    reader.readAsDataURL(droppedFiles[0]);

    // Set the selected file in the hidden input (optional)
    profileImageInput.files = droppedFiles;
  });

  // Handle click on "
  profileImageDropzone.addEventListener("click", () => {
    profileImageInput.click();
  });

  profileImageInput.addEventListener("change", function () {
    const file = profileImageInput.files[0];
    const reader = new FileReader();
    reader.onload = function (e) {
      previewImage.src = e.target.result;
    };
    reader.readAsDataURL(file);
  });
} catch (error) {
  console.log(error);
}

try {
  const fileUpload = document.getElementById("file-upload");
  const filePreview = document.getElementById("file-preview");
  const fileName = document.getElementById("file-name");
  const fileSize = document.getElementById("file-size");
  const fileType = document.getElementById("file-type");
  const fileContainer = document.getElementById("file-container");

  fileUpload.addEventListener("change", () => {
    const file = fileUpload.files[0];
    if (file) {
      fileName.textContent = file.name;
      // get file size
      fileSize.textContent = `${(file.size / 1024).toFixed(2)} KB`;
      fileType.textContent = file.type ? ` | ${file.type}` : "";

      filePreview.classList.remove("hidden");
    } else {
      filePreview.classList.remove("show");
    }
  });

  fileContainer.addEventListener("dragover", (e) => {
    e.preventDefault();
    fileContainer.classList.remove("bg-white");
    fileContainer.classList.add("bg-gray-200");
  });

  fileContainer.addEventListener("dragleave", (e) => {
    e.preventDefault();
    fileContainer.classList.remove("bg-gray-200");
  });

  fileContainer.addEventListener("drop", (e) => {
    e.preventDefault();
    const droppedFiles = e.dataTransfer.files;
    fileUpload.files = droppedFiles;
    fileContainer.classList.remove("bg-gray-200");
    fileUpload.dispatchEvent(new Event("change"));
  });

  fileContainer.addEventListener("click", () => {
    fileUpload.click();
  });
} catch (error) {
  console.log(error);
}

try {
  const addProgrammeButton = document.getElementById("add-programme");
  const programmeEntries = document.querySelectorAll(".programme-entries");
  let formCounter = programmeEntries.length;
  const removeButton = document.querySelectorAll(".remove-button");

  addProgrammeButton.addEventListener("click", function () {
    formCounter++;

    const newProgrammeEntry = programmeEntries[0].cloneNode(true);
    newProgrammeEntry.id = `programme-entries-${formCounter}`;

    // Update field names and IDs within the new form
    newProgrammeEntry.querySelectorAll("select, input").forEach((element) => {
      const originalName = element.name;
      const newName = originalName.replace(/-\d+/, `-${formCounter}`);
      element.name = newName;
      element.id = newName;

      if (element.type !== "hidden") {
        element.value = ""; // Clear the value for new entries
      }
    });

    // Clear hidden field value
    newProgrammeEntry.querySelector('input[type="hidden"]').value =
      formCounter + 1;

    programmeEntries[0].parentNode.parentNode.append(newProgrammeEntry);
  });
} catch (e) {
  console.log(e);
}

try {
  // static/js/scripts.js
  document.addEventListener("DOMContentLoaded", function () {
    var modal = document.getElementById("confirmationModal");
    var closeModalBtn = document.getElementsByClassName("close-button")[0];
    var cancelBtn = document.getElementById("cancelButton");
    var openModalBtns = document.getElementsByClassName(
      "open-confirmation-modal"
    );

    for (var i = 0; i < openModalBtns.length; i++) {
      openModalBtns[i].onclick = function () {
        var actionUrl = this.getAttribute("data-action-url");
        document.getElementById("confirmationForm").action = actionUrl;
        modal.style.display = "block";
      };
    }

    try {
      if (closeModalBtn !== undefined && cancelBtn !== undefined) {
        closeModalBtn.addEventListener("click", function () {
          modal.style.display = "none";
        });

        cancelBtn.addEventListener("click", function () {
          modal.style.display = "none";
        });
      }

      window.addEventListener("click", function (event) {
        if (event.target == modal) {
          modal.style.display = "none";
        }
      });
    } catch (error) {
      console.error(error);
    }
  });
} catch (error) {
  console.error(error);
}

try {
  /**
   * Validates the input value.
   * @param {string} value - The input value to be validated.
   * @returns {boolean} - Returns true if the value is a valid number, otherwise false.
   */
  const validateInput = (value) => {
    const newValue = +value;
    return !isNaN(newValue) && newValue !== 0;
  };

  /**
   * Formats the input value to match the GHA-XXXXXXXXX-X pattern.
   * @param {string} value - The input value to be formatted.
   * @returns {string} - The formatted value.
   */
  const ghCardFormat = (value) => {
    // Ensure the value is trimmed and only takes the necessary part
    value = value.replace(/[^\d]/g, "").slice(0, 10); // Only take the first 10 digits
    return `GHA-${value.slice(0, 9)}-${value.slice(9)}`;
  };

  const input = document.getElementById("identification_number");
  const type = document.getElementById("identification_type");

  type.addEventListener("change", (e) => {
    const value = e.target.value;
    if (value == "1") {
      type.value = "1";
      input.placeholder = "GHA-XXXXXXXXX-X";
      input.placeholder = "GHA-XXXXXXXXX-X";
    input.addEventListener("keyup", (e) => {
      const value = e.target.value;

      if (validateInput(value.replace(/[^\d]/g, ""))) {
        if (value.length <= 15) {
          input.value = ghCardFormat(value.replace(/[^0-9]/g, ""));
        } else {
          e.preventDefault();
          input.value = input.value.slice(0, 15);
        }
      } else if (value.startsWith("GHA-")) {
        if (value.length === 13) {
          const newValue = value.slice(0, 14) + "-" + value.slice(14);
          input.value = newValue;
        }
      } else {
        e.preventDefault();
        input.value = "";
      }
    });
    } else {
      input.placeholder
    }
  })

  if (type.value == "1") {
    input.placeholder = "GHA-XXXXXXXXX-X";
    input.addEventListener("keyup", (e) => {
      const value = e.target.value;

      if (validateInput(value.replace(/[^\d]/g, ""))) {
        if (value.length <= 15) {
          input.value = ghCardFormat(value.replace(/[^0-9]/g, ""));
        } else {
          e.preventDefault();
          input.value = input.value.slice(0, 15);
        }
      } else if (value.startsWith("GHA-")) {
        if (value.length === 13) {
          const newValue = value.slice(0, 14) + "-" + value.slice(14);
          input.value = newValue;
        }
      } else {
        e.preventDefault();
        input.value = "";
      }
    });
  }
} catch (error) {
  console.error(error);
}
