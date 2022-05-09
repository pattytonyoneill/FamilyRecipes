from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import Recipe_form
from .forms import CommentForm

def create_recipe(request):
    if request.method == "GET":
        form = Recipe_form()
        formset = IngredientsFormSet()
        return render(request, 'create_recipe.html', {"form":form, "formset":formset})

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def recipe(self, request, slug, *args, **kwargs):
