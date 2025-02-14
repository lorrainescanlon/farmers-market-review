const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

/**const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality.
* 
* For each button in `editButtons`:
* - Retrieve the review's ID on click.
* - Retrieve the content of the review.
* - Populate the `reviewText` textarea review content for editing.
* - Update the submit button's text to "Update".
* - Set the form's action attribute to the `edit_review/{reviewId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    let reviewContent = document.getElementById(`review${reviewId}`).innerText;
    reviewText.value = reviewContent;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}


/**
* Initializes delete functionality
* 
* For each button in `deleteButtons`:
* - Retrieve the review's ID upon click.
* - Update the `deleteConfirm` link's href to point to the 
* deletion endpoint for the review.
* - Display a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("review_id");
      deleteConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
  }
    */