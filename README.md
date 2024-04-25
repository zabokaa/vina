# :purple_circle: *Viña - your vinotheque* :purple_circle:

Have you ever found yourself standing in front of the overwhelming wine cupboard in a supermarket, not knowing what to buy? Me: Yes! And my friends too. I was imagining how great it would be to have an app that serves as both my private wine library and a platform for showcasing.

 ![mockup](./assets/imgreadme/vinamockup.png)

🍷 The deployed page can be found [here](https://vina1312-ae94d8859b43.herokuapp.com/) 🍷

If you do not want to register for testing the Viña App feel free to use:
<Username: Winelover>
<Password: oenology>

## Table of Contents

- [Objective](#objective)
- [User Stories](#user-stories)
- [Key Features](#key-features)
- [Database](#database)
- [Design](#design)
- [Testing](#testing)
  - [Manual](#manual)
  - [Official Validators](#official-validators)
  - [Bugs](#bugs)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Project Status](#project-status)
- [Acknowledgements](#acknowledgements)

## Objective

- Hands-on learning by building an interactive, data-based web app
- To offer a help for users to decide which bottle of wine to buy
- Creating a platform for wine lovers to share their recomendations as well as their experiences

## User Stories

### As a Logged-in-user [...]

- I want to add and delete wines to my private library/vinotheque.
- I want to commment on my own or others users' post.
- I want to be able to edit or delete my comments.
- I want to see if I am logged-in or not.
- I want to lika and unlike Posts.
- I want to see the list of all my liked Posts, and being transferred to that one when clicking on it. 
- I want to be transferred to the Post when 
- I expect a consistent and responsive design for easy use on various devices, prioritizing mobile devices first.

### As a Guest-user [...]

- I want to read recommendations (posts and comments).
- I want to easily navigate the site.
- I want to be able to create my own profile.

### As a Super-user = Admin [...]

- I want to to approve or disapprove user's new entries/posts
- I want to approve or dissaprove comments on existing entries.

## Key Features

### Menu

### Pre-Entry Page

  ![intro](./assets/imgreadme/agever.png)

- The welcome page has a age verification.
- Validating for entry and age >= 18.
- Header not displaying navbar links in order not to be able to avoid age validation.

### Header

  ![header](./assets/imgreadme/header.png)

### Home (= all Posts)

   ![home](./assets/imgreadme/bloghome.png)

- Displaying all wine blog entries
- Pagination = 4 with previous and next buttons

#### Details of 1 specific Post with like/unlike Function

  ![detailwine](./assets/imgreadme/wineentry.png)

- Displaying details of one wine
- Like/unlike Button -> will be added/deleted to favorite wine list
- Back Home button -> for better UX

#### Create / Edit / Delete a Comment

  ![edit](./assets/imgreadme/updatecom.png)

### User Login

  ![signin](./assets/imgreadme/signin.png)

- Unlogged user will be transferred to Sign In when trying to add comment or use like/unlike button.

### My Vinotheque

#### List of Liked Post

  ![listofliked](./assets/imgreadme/listofliked.png)

#### Create new Diary Entry

  ![newdiary](./assets/imgreadme/newdiary.png)

- Form with validation for rating and date-format.

#### Overview of Diary Entries

  ![diarylist](./assets/imgreadme/diarylist.png)

- Table of diary entries, ordered by rating.
- Name is linking to details of this diary entry.

#### Details of 1 Diary Entry

  ![onediary](./assets/imgreadme/deletediary.png)

- Display wine diary entry with picture (placeholder pic or if it exists uploaded pic by user).
- Delete entry or back to vinotheque buttons.
- Modal for delete action.

### Footer

  ![footer](./assets/img/footer.png)

- The footer contains a short impressum and links to social media accounts.

## Database

    ![ERD](./assets/imgreadme/xx.png)

## Design

### Colors

### Logo

## Testing

### Manual

### Official Validators

- [W3C HTML Validator](./assets/img/htmlVal.png): No errors
- [W3C CSS Validator](./assets/img/CSSvalidator.png):  No errors
- [Lighthouse Chrome DevTools](./assets/img/lighthouseVal.png): Accessibility 100
- [WAVE](./assets/img/WAVEval.png): No errors for accessibility and color contrast

### Automated

### Bugs

#### Solved

#### Unsolved

## Technologies

Python | HTML | CSS | JavaScript | Django | Bootstrap5 | Whitenoise | Gunicorn | Crispy | Neon Postgres DB | Heroku

## Project Status

Project is: in process

## Deployment

- The site is deployed with Heroku.

  HOW TO:

  1. **Go to Repository Settings:**
  
  2. **Scroll Down to GitHub Pages Section:**
     In the Settings, scroll down to the "GitHub Pages" section.
  
  3. **Choose Your Source Branch:**
     Under "Source," select the branch you want to use for GitHub Pages (e.g., `main`).
  
  4. **Save Your Changes:**
     Save the changes. GitHub Pages will provide you with a link to your deployed site.
  
  5. **Wait for the Build:**
     GitHub Pages will now build and deploy your site. Wait for the process to complete.
  
  6. **Access Your Deployed Site:**
     Once the build is successful, you can access your deployed site using the provided link.

  Your project is now live on GitHub Pages!
  🍷 Cheers !!

## Acknowledgements

This project is based on full-stack course @ Code Institute, especially the Walk-through-project "I Think Therefore I Blog"

Creating ERD of whole project with Djangoviz: [Source here](https://atlasgo.io/blog/2023/05/17/djangoviz)
