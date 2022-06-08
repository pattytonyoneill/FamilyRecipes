from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts", default=''
    )
    featured_image = CloudinaryField('image', default='placeholder')
    directions = models.TextField()
    prep_time = models.DurationField()
    cook_time = models.DurationField()

    servings = models.IntegerField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_like', blank=True)

    def __str__(self):
        return f"{self.title} recipe by {self.author}"


class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    measure = models.CharField(max_length=50)

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ingredients"


class Comment(models.Model):
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
