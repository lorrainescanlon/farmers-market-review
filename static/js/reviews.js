const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Model(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes functionality for the review edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieve the associated review's id when clicked.
 * - Retrieve the review content for that review id.
 * - Populate the `reviewText` textarea with the review content for editing.
 * - Update the submit buttons text to "Update".
 * - Set the forms action attriute to the `edit_review/{reviewId}` endpoint.
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
 * Initializes delete button functionality.
 * 
 * for each button in `deleteButtons`:
 * - Retrieve the assocaited review id upon click.
 * - Update the `deleteConfirm` links href to point to the 
 * deletion endpoint for the specific review.
 * - Display a confirmation modal (`deleteModal`) to prompt
 * the user for confirmation before deletion. 
 */

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review_id");
        deleteConfirm.href = `delete_review/${reviewId}`;
        deleteModal.show();
    })
}