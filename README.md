# [Our Family Recipes]
- ![image](static/images/different_device.jpg)
## Visit the live Website : **[Family Recipes :arrow_right:](https://family-recipes14.herokuapp.com/)**
- Family Recipes that are to be shared amoung family and friends.
- Users will be able to comment on and add useful suggestions of ways that the recipe can be improved.

User Stories:
- _First time Visitor Goals_
  As a first time user of this site, I would like to be able to easily create a draft of a recipe.
  - As a first time user, I would like to be able to comment on recipes.
  - As a first time user, I would like to Like/Unlike the recipes.
  - As a first time user, I would like to be able to view likes.
  - As a first time user, I would like to view comments on the recipes.
  - As a first time user, I would like to easily register.
  - As a first time user, I would like to view a paginated list of recipes so that I can select which post I want to view.
  - As a first time user, I would like to be able to edit and delete my comments.

## Existing Features
- Interactive Elements:
  - Home page
    - ![image](static/images/home_page.jpg)
  - Login/Logout
    - ![image](static/images/login_page.jpg)
    - ![image](static/images/log_out.jpg)
  - Register
    - ![image](testing/register_page.jpg)
  - Like
    - ![image](static/images/like_comment.jpg)
  - Comment
    - ![image](static/images/like_comment.jpg)
  - Ability to edit/delete comments
    - ![alt-text-for-image](testing/edit_delete.png)

## Languages Used:

- Python
- Django
- HTML
- CSS
- JavaScript

## Relational Database used:

- Postgres

## Frameworks, Libraries & Programs Used:

- [Git](https://git-scm.com): used to utilize the Gitpod terminal to commit to Git and Push to GitHub
- [GitHub](https://github.com/): used to store project code after being pushed from Git
- [GitPod](https://gitpod.io/): used as cloud based IDE for writing code
- [Balsamiq Wireframes](https://balsamiq.com/):  used to draw wireframes of pages of project
- [Am I Responsive?](http://ami.responsivedesign.is/) used to give a visual of what the project looks like on various devices
- [Heroku](https://heroku.com): used to deploy the Our Family Recipes app
- [Cloudinary](https://cloudinary.com/): used to import my Cloudinary field for the featured image
- [Diffchecker](https://www.diffchecker.com/): used to compare code when I had an error

### Wireframes
To view all wireframes, go to [WIREFRAMES.md](WIREFRAMES.md)

## Deployment

The live deployed application can be found at [family-recipes14.herokuapp.com](https://family-recipes14.herokuapp.com/).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the following key/value pairs:
  - `CLOUDINARY_URL` (insert your own Cloudinary API key here)
  - `DATABASE_URL` (this comes from the **Resources** tab, you can get your own Postgres Database using the Free Hobby Tier)
  - `SECRET_KEY` (this can be any random secret key)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: gunicorn family_recipes.wsgi > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

Either:
- Select "Automatic Deployment" from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku.

### Local Deployment

*Gitpod* IDE was used to write the code for this project.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/FamilyRecipes.git`

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/FamilyRecipes)

## Future Additions to page
- put drop down menu to have user choose minutes and hours for the cooking time and prep time
- put drop down menu to have user choose measurement type
- have measurements able to be converted from metric to US standard
- add ability to put fractions in recipes
- have the user be able to add recipes of their own

## Credits
-  [Create a Recipe App](https://engineertodeveloper.com/getting-started-with-django-forms-create-a-recipe-app/)
-  [Update View -Function based Views Django](https://www.geeksforgeeks.org/update-view-function-based-views-django/)

### Code
- _Readme used sample readme from code institute as a model. [Github](https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md)_

### Content
- _All content written by the developer._

### Acknowlegements
- _My Mentor for his help and feedback._
- _Tutor support at Code Institute_
- _Family for help with help and feedback on website as a user_

## Data Schema
- ![image](testing/data_schema.jpg)

#### Testing

To view all testing, go to [TESTING.md](TESTING.md)