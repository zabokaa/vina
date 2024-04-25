# Testing Guide

## Navigation



| Feature | Action                             | Expected Result                 | Status of Actual Result    |
| :-----: | :---------------------------------:| :------------------------------:|
| **Home Link Icon** | While not on the homepage, click the icon. | User is redirected back to homepage. |
| **"Login" Link** | While not authenticated, click "Login". | User is directed to the Login page. |
| **"Sign Up" Link** | While not authenticated, click "Sign Up". | User is directed to the Sign Up page. |
| **"Game Details" Link** | Click on any game. | User is directed to the Game Detail page. |
| **"Like" Link** | While authenticated, click on the thumb up. | Thumb fills color to orange |
| **"unlike" Link** | While authenticated, click on the thumb up. | Thumb up filling disappears. |
| **"Social Links" Link** | click "Social Links". | Opens new page in Browser and redirects to social media page. |
| **"Logout" Link** | While authenticated, click "Logout". | User is directed to Logout Page |

## CRUD

The full CRUD functionality is only available to logged-in users.

### Create

Write and submit a new comment via the comment submit form on the review detail page (logged-in users only)

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Content field** | Select the field and start typing. | Written text displays. |
| **Submit** | After completing the comment form, click the submit button. | The alert message informs the user that the comment awaits approval. |
| **Incomplete form** | clicking on the submit button without filling email or Body field | Message is displayed to make sure to fill the field |
| **View Comment** | After submitting a comment, wait for admin approval | Once admin has approved submission, the comment can now be seen below review |


### Read

Read Reviews

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Game card/ Review card** | On the index page, click on any game. Then click on any review | Review is displayed |


### Update

Option to edit existing comments after clicking edit button (logged-in users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|

| **Edit-Butttn** | On the review detail page, click the edit button next to a comment. The button is only visible after login. | Directs to  comment edit page where the original comment is displayed. |
| **Submit** | Change comment or leave it as it is. | User is re-directed to the review detail page with the newly edited or old comment showing. |


### Delete

Option to delete existing comments after clicking delete button (logged-in users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Delete-Button** | On the review detzail page, click the delete button next to your comment. | review detail page only shows the delete button of the user's own comments to ensure users can only delete their own comments. |
| **Confirm Delete** | On the delete page, click "Delete". | User is re-directed to the review detail page, selected comment has been deleted. |
| **Cancel** | On the delete page, click "Cancel". | User is re-directed to review detail page with no delete action taken. |


## Sign Up

Account creation for unauthenticated users.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Sign Up form** | Go to Sign Up page via nav link | Renders form input fields Username, Email (optional), Password, Password (confirm). |
| **Submit** | Fill in form fields accordingly. Click "Sign Up". | Self-closing message informs the user of successful account creation, including username. The user is re-directed to the homepage and navigation shows links for authenticated users and textfiled showing name of logged in user. |
| **Incomplete form** | Failing to fill out all form fields, click "Sign Up". | User remains on the Sign-Up form view and is prompted to complete missing fields. |

## Login

Signing into an existing account (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Login form** | Go to the Login page via nav link | Renders form input fields Username, Password, Remember me (checkbox). |
| **Submit** | Fill in form fields accordingly. Click "Sign In". | Self-closing message informs the user of a successful login, including username. The user is re-directed to the homepage and navigation shows links for authenticated users. |
| **Incomplete form** | Failing to fill out all form fields, click "Sign In". | User remains on the Sign-Up form view and is prompted to complete missing fields. |
| **Remember me** | When signing in, tick "Remember me". Log out and sign in again. | Login form is pre-populated with username and hidden password. |

## Logout

Allows users to sign out of existing accounts (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Logout form** | When authenticated, go to the Logout page via the nav link | User is directed to the Logout page, asking the user to confirm the action. |
| **Sign Out** | On the Logout page, click "Sign Out". | Self-closing message informs the user of successful logout. The user is re-directed to the homepage and navigation shows links for unauthenticated users. |


## Liking

Option to like/unlike reviews (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Like** | In the review detail page, click the like button (thumb up icon) below the text of a review that isn't already liked. | Icon fills color to orange. Like count is incremented by 1. |
| **Unlike** | In the review detail view, click the like button (thumb up icon) below the text of a review that is already liked. | Icon goes back to without orange filling. Like count is decremented by 1. |

## Social Links

Links to social media sites are located in the footer (available to all users).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Link Icons in Footer** | Click on any of the social media icons | New tab opens with respective social media site |