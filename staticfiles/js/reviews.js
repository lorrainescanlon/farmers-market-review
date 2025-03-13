const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Initializes edit functionality for review buttons.
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("value");
    let reviewContent = document.getElementById(`review${reviewId}`).innerText;
    reviewText.value = reviewContent;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}


// Initializes delete functionality for delete buttons.
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("value");
      deleteConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
  }
  