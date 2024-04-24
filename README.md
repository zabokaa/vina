# :purple_circle: *Viña - your vinotheque* :purple_circle:

Have you ever found yourself standing in front of the overwhelming wine cupboard in a supermarket, not knowing what to buy? Me: Yes! And my friends too. I was imagining how great it would be to have an app that serves as both my private wine library and a platform for showcasing recommendations from my friends. Even better, with their stories of the evening added - helping me remember which wine I like.

 ![mockup](./assets/imgreadme/vinamockup.png)

🍷 The deployed page can be found [here](https://vina1312-ae94d8859b43.herokuapp.com/) 🍷

If you do not want to register for testing feel free to use:
<Username: Winelover>
<Password: oenology>

## Table of Contents

- [Objective](#objective)
- [User Stories](#user-stories)
- [Key Features](#key-features)
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

### Start Page

  ![intro](./assets/img/intro.png)

- The page has the title 'FeministQuiz,' and after the welcoming, there is a short description about the topic of the quiz.
- Below, the user sees a box displaying the rules of the quiz.

### User Login

  ![username](./assets/img/startQuiz.png)

### Home (= all Posts)

### Register

  ![modal](./assets/img/modal.png)

### My Vinoteka

  ![endQuiz](./assets/img/scoreAgain.png)

### Footer

  ![footer](./assets/img/footer.png)

- The footer contains a short impressum and my email address in case the user wants to contact me.

## Design

### Colors

### Typography

I did research about feminist typography and picked two fonts out of those suggestions. The font used for the headline is reminiscent of historical typefaces and therefore fits well for a quiz on the history of feminist achievements in Germany.

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
