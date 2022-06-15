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
-  Pep8 for models.py
     - ![image]()
-  Pep8 for test.py
     - ![image]()
-  Pep8 for views.py
     - ![image]()

## Remaining Bugs
- 

## Bugs
- No module named 'recipe'.  Looked through code until I found where I needed to add recipe in urls.py.
     -![image](testing/name_error.jpg)
- NoReverseMatch at /test-recipe/. I had to add a url to my recipes/urls.py
     -![image](testing/no_reverse_match.jpg)
- Nullable field 'author' on recipe to non nullable field. I edited code until this error was corrected.
     -![image]testing/nullable_field_author.jpg)

Return back to [README.md](README.md)