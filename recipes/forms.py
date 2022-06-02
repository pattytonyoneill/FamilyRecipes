from django import forms
from .models import Recipe, Ingredients, Comment


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        exclude = ('recipes',)


IngredientsFormSet = forms.inlineformset_factory(
    Recipe, Ingredients, form=IngredientsForm)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
