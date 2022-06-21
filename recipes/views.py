from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Recipe, Ingredients, Comment
from .forms import RecipeForm, CommentForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

    def recipe(self, request, slug, *args, **kwargs):
        def create_recipe(request):
            if request.method == "GET":
                form = Recipe_form()
                formset = IngredientsFormSet()
                return render(
                    request, 'create_recipe.html',
                    {"form": form, "formset": formset})


class RecipeDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        ingredients = Ingredients.objects.filter(recipe=recipe)
        comments = recipe.comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "ingredients": ingredients,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        ingredients = Ingredients.objects.filter(recipe=recipe)
        comments = recipe.comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = recipe
            comment.save()
        else:
            comment_form = CommentForm()
        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "ingredients": ingredients,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class RecipeLike(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment_form = CommentForm(request.POST or None, instance=comment)

    if request.method == "POST":
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "Commented updated!")
            return redirect(reverse("recipe_detail", args=[comment.post.slug]))
        messages.error(request, "Error. Please try again.")
    template = "edit_comment.html"
    context = {
        "comment": comment,
        "comment_form": comment_form,
    }
    return render(request, template, context)


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Commented deleted!")
        return redirect(reverse("home"))
