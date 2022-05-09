from django import forms
from .models import Recipe, Comment

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        exclude = ('recipe',)

IngredientsFormSet = forms.inlineformset_factory(Recipe, Ingredients, form=IngredientForm)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)