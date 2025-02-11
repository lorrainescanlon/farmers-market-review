const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

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