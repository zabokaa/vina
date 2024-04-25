# Testing Guide

## User Stories Testing

### As a Guest-user

| Test Case Description | Steps to Reproduce | Expected Result | Actual Result |
| --------------------- | ------------------ | --------------- | ------------- |
| Read recommendations  | Navigate to the homepage --> Click on a post | The post's details are displayed, including comments. | [ ] |
| Navigate the site     | Click on different navigation links --> Scroll up and down on different pages | The site is easy to navigate and all links work correctly. | [ ] |
| Create a profile      | Click on the "Sign Up" link --> Fill out the form and submit it | A new profile is created and the user is logged in. | [ ] |

### As a Logged-in-user

| Test Case Description | Steps to Reproduce | Expected Result | Actual Result |
| --------------------- | ------------------ | --------------- | ------------- |
| Add wine to library   | Log in --> Navigate to the library page --> Click on the "Add Wine" button --> Fill out the form and submit it | The new wine is added to the library. | [ ] |
| Comment on a post     | Log in --> Navigate to a post --> Fill out the comment form and submit it | The new comment is added to the post. | [ ] |
| Edit a comment        | Log in --> Navigate to a comment you made --> Click on the "Edit" button --> Modify the comment and submit the form | The comment is updated. | [ ] |

### As a Super-user = Admin

| Test Case Description | Steps to Reproduce | Expected Result | Actual Result |
| --------------------- | ------------------ | --------------- | ------------- |
| Approve a post        | Log in as an admin --> Navigate to a new post --> Click on the "Approve" button | The post is approved and visible to all users. | [ ] |
| Disapprove a comment  | Log in as an admin --> Navigate to a comment --> Click on the "Disapprove" button | The comment is disapproved and no longer visible to users. | [ ] |