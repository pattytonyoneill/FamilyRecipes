from django.contrib import admin
from .models import Recipe, Ingredients, Comment
from django_summernote.admin import SummernoteModelAdmin


class IngredientsInline(admin.TabularInline):
    model = Ingredients


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientsInline, ]
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Ingredients)
