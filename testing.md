
# User Stories Testing

## As a Guest-user

| Test Case Description | Steps to Reproduce | Expected Result | Actual Result |
| --------------------- | ------------------ | --------------- | ------------- |
| Read recommendations  | Navigate to the homepage. To see the Wine details --> Click on the name of the post | The post's details are displayed, including comments. | [ True ] |
| Navigate the site     | Click on different navigation links and Social Media Links in the footer| The site is easy to navigate and all links work correctly. | [  True] |
| Create a profile      | Click on the "Sign Up" link --> Fill out the form and submit it | A new profile is created and the user is logged in. | [ True ] |

## As a Logged-in-user

| Test Case Description | Steps to Reproduce | Expected Result | Actual Result |
| --------------------- | ------------------ | --------------- | ------------- |
| Add and delete wine to library   | Open Wine details of 1 Post --> Click on the like/unlike heart | The new wine is added to the library and the heart-text changed accordingly | [  True ] |
| Comment on a post     | Open Wine details of 1 Post --> Fill out the comment form -> Click on "Submit" button | The new comment will be displayed in a lighter color with the reminder "This comment is waiting for approval". | [  True ] |
| Edit my comments | Click on the "Edit" button below a comment you made --> Modify the comment and click on "Update" button | The comment is visible in the comment form. It is working for approved and not-approved ones. After updating the comment will be displayed with "This comment is waiting for approval" message | [  True ] |
| Delete my comments | Click on the "Delete" button below a comment you made --> Click on the "Delete" button in the "Delete coment?" modal | The "Delete comment?" modal will show up. If user does not want to delete, they "Close" the modal. If want to delete click on the "Delete" button, the comment (approved or not-approved) is not visible anymore. Django message confirmation | [  True ] |
| See if I am logged-in or not | Log in --> Check the user status indicator on the right top of the site | The indicator shows that the user is logged in or not, if logged in it will also dispaly the username: "Hola jochy 🍷 you are logged-in" | [ True ] |
| See the list of all my liked Posts, and being transferred to that one when clicking on it | Navigate to "My Vinotheque". If wanted: click on a list item navigates to that post | A list of all liked posts is displayed, and clicking on the name of the liked wine navigates to that post | [ True ] |

| Create a new Wine Diary entry, where I can decide by myself if I want to add an image, a memory text, or a foodpairing hint | Navigate to "My Vinotheque" --> Fill out the form and submit it | Validation check for required entries first. Then a new diary entry is created  | [ True ] |
| See a list of all my diaries (or "nor entries yet" when there are none) with name of wine, ordered by my rating | Navigate to "My Vinotheque" | A table with all diary entries is displayed, ordered by rating | [ True ] |
| Display the specific diary entry when clicking on the name | Navigate to "My Vinotheque" --> Click on a diary entry name | The details of the diary entry are displayed on a new site. If user has uploaded their own image when creating the diary entry it will be displayed, if not the standard image will be shown | [  True ] |
| Delete a diary entry | Navigate to "My Vinotheque" --> Click on a diary entry name --> Click on the "Delete" button on the redirected site | The user will be redirected to the specific diary entry site. After clicking "Delete" The "Delete comment?" modal will show up. If user does not want to delete, they "Close" the modal.The diary entry is deleted | [ True ] |

## As a Super-user = Admin

| Test Case Description | Steps to Reproduce | Expected Result | Actual Result |
| --------------------- | ------------------ | --------------- | ------------- |
| Write a post        | Log in as an admin --> Create a new post --> Click on the "Approve" button | The post is approved and visible to all users. | [  True ] |
| Approve a comment  | Log in as an admin --> Navigate to a comment --> Click on the "Approve" button | The post is approved and visible to all users. | [  True ] |