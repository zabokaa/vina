# :purple_circle: *Viña - your vinotheque* :purple_circle:

Have you ever found yourself standing in front of the overwhelming wine cupboard in a supermarket, not knowing what to buy? Me: Yes! And my friends too. I was imagining how great it would be to have an app that serves as both my private wine library and a platform for showcasing recommendations from my friends. Even better, with their stories of the evening added - helping me remember which wine I like.

 ![mockup](./assets/img/mockup.png)

🍷 The deployed page can be found [here](https://xxxx) 🍷

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
- I want to add a new entry (= post) for a wine.
- I want to upload an image of the wine bottle.
- I want to commment on my own or others users' post.
- I expect a consistent and responsive design for easy use on various devices, prioritizing mobile devices first.

### As a Guest-user [...]

- I want to read recommendations (posts and comments).
- I want to be informed about the aim of the page.
- I want to easily navigate the site.
- I want to be able to create my own profile.

### As a Super-user = Admin [...]

- I want to to approve or disapprove user's new entries/posts
- I want to approve or dissaprove comments on existing entries.

## Key Features

### Start Page

  ![intro](./assets/img/intro.png)

- The page has the title 'FeministQuiz,' and after the welcoming, there is a short description about the topic of the quiz.
- Below, the user sees a box displaying the rules of the quiz.

### User Login and Start Quiz

  ![username](./assets/img/startQuiz.png)

- After entering a username, the user can press the "Start the Quiz" button, and the quiz section will be displayed.
- In case the user did not set a username, the following alert will be displayed: "Please enter your username before starting the quiz 💪" to inform the user about the required step.
- At the end of the round, the user's score will be displayed with an encouraging quote using their username to make it more personal.

### Quiz Section

  ![quizValidation](./assets/img/questionIncorrect.png)

- The question will be displayed with three answers to choose from.
- Moving to one answer box, the color of that box will change, as well as the cursor.
- After choosing one answer, the "More Info" as well as the "Next" button will pop up.
- There is no go home etc. button becuase I like the user to finish the quiz.
- The user knows where they are in the quiz: The questions are numbered.

### Modal for background info about correct answer

  ![modal](./assets/img/modal.png)

- In case the user wants to get more background information regarding the correct answer, they can press the "More Info" button, and it will be shown in a modal box.
- The user can choose for themselves if they want to spend time reading that or not.
- It can be closed with the close button inside.

### End of Game Round --> Score and Play again

  ![endQuiz](./assets/img/scoreAgain.png)

- The user's score will be displayed in the form of "x out of 5" correct answers, below which there will be a personalized message.
- On top of that box, the user can find the 'Start a New Round' button.

### Footer

  ![footer](./assets/img/footer.png)

- The footer contains a short impressum and my email address in case the user wants to contact me.

## Design

### Colors

As primary and secondary colors, I chose purple and green (here with a more bluish tone) because they are two colors globally connected to feminist movements.

  ![colorpalatte](./assets/img/ColorPalate.png)

For indicating the correct and incorrect answer of each questions I use green and red because the colors are self-explanatory in this context. I chose a pastel colour in each case because it is easier to integrate into the colour palette of the page.

### Typography

I did research about feminist typography and picked two fonts out of those suggestions. The font used for the headline is reminiscent of historical typefaces and therefore fits well for a quiz on the history of feminist achievements in Germany.

## Testing

### Manual

- Navigation is working.
- After entering a username, the user can press the "Start the Quiz" button.
- The intro section will not be displayed while showing the quiz section.
- If a username has been entered, it is stored for the next round.
- "Next" and "Modal" buttons are only displayed after the user has selected an answer.
- The user can only select one answer.
- The "Modal" button ("More Info") can be closed manually, and if the user did not, it will close when displaying the next question.
- Questions are picked randomly for each new round.

### Official Validators

- [W3C HTML Validator](./assets/img/htmlVal.png): No errors
- [W3C CSS Validator](./assets/img/CSSvalidator.png):  No errors
- [Lighthouse Chrome DevTools](./assets/img/lighthouseVal.png): Accessibility 100
- [WAVE](./assets/img/WAVEval.png): No errors for accessibility and color contrast

### Bugs

- When a user wants to restart the game the shuffle funcion was not called. I fixed the bug by moving `randomize(questions);` to the `openQuiz()` function.

- When user did not close the modal box it has been displayed (beiing open) on the next slide. I fixed it using following if-statment `if (modal.style.display === "block") {
        modal.style.display = "none";
    }`

## Technologies

Python | HTML | CSS | JavaScript | Django

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

## Acknowledgements

This project was based on full-stack course @ Code Institute.

Ideas for code snippets (commented in my code)

- [W3School](https://www.w3schools.com/howto/howto_css_modals.asp) [for modal code]
- [Web Dev Simplified](https://www.youtube.com/watch?v=riDzcEQbX6k) [as quoted in script.js]

The content of some questions are taken from:

- [GeoWissen](https://www.geo.de/wissen/quiz/quiz-was-wissen-sie-uber-die-frauenbewegung-30203104.html) [translated by me]
- [Amnesty International](https://www.amnesty.de/sites/default/files/2019-03/Quiz-Frauenrechte-2019.pdf) [translated by me]
