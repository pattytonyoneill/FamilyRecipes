from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Ingredients
from .forms import RecipeForm
from .forms import CommentForm


class RecipeList(generic.ListView):
    model = Recipe
    template_name = 'index.html'
    paginate_by = 6
    def recipe(self, request, slug, *args, **kwargs):
        def create_recipe(request):
            if request.method == "GET":
                form = Recipe_form()
                formset = IngredientsFormSet()
                return render(request, 'create_recipe.html', {"form":form, "formset":formset})
    
