# [Our Family Recipes](https://our-family-recipes14.herokuapp.com/)
# Testing for Our Family Recipes

## User Stories testing:
- _First time Visitor Goals_
  - As a first time user of this site, I would like to be able to easily create a draft of a recipe.
  - As a first time user, I would like to be able to comment on recipes.
  - As a first time user, I would like to Like/Unlike the recipes.
  - As a first time user, I would like to be able to view likes.
  - As a first time user, I would like to view comments on the recipes.
  - As a first time user, I would like to easily register.
  - As a first time user, I would like to view a paginated list of recipes so that I can select which post I want to view.

## Testing
- 
    - ![image]()

## Validator Testing
###Pep8
-  Pep8 for models.py
     - ![image](testing/models.py.jpg)
-  Pep8 for forms.py
     - ![image](testing/forms.py.jpg)
-  Pep8 for admin.py
     - ![image](testing/admin.py.jpg)
-  Pep8 for test.py
     - ![image]()
-  Pep8 for views.py
     - ![image](testing/views.py.jpg)
-  Pep8 for recipes/apps.py
     - ![image](testing/recipes.apps.py.jpg)
-  Pep8 for recipes/urls.py
     -  ![image](testing/recipes.urls.py.jpg)
-  Pep8 for wsgi.py
     -  ![image](testing/wsgi.py.jpg)
-  Pep8 for FamilyRecipes/urls.py
     -  ![image](testing/FamilyRecipes.urls.py.jpg)
-  Pep8 for settings.py
     -  ![image]()
-  Pep8 for env.py
     -  ![image]()
-  Pep8 for manage.py
     -  ![image]()

## Remaining Bugs
-

## Bugs
- No module named 'recipe'.  Looked through code until I found where I needed to add recipe in urls.py.
     -![image](testing/name_error.jpg)
- NoReverseMatch at /test-recipe/. I had to add a url to my recipes/urls.py
     -![image](testing/no_reverse_match.jpg)
- Nullable field 'author' on recipe to non nullable field. I edited code until this error was corrected.
     -![image](testing/nullable_field_author.jpg)
- Forbidden CSRF Verification failed. I added  the code for CSRF_TRUSTED_ORIGINS  to settings.py.
     -![image](testing/csrf.jpg)
- Integrity Error. I needed to correct where I had recipe instead of post.
     -![image](testing/integrity.jpg)
- Page Not Found error.  I reviewed and edited code.
     -![image](testing/likesError.jpg)


Return back to [README.md](README.md)