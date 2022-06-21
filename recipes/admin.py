from django.contrib import admin
from .models import Recipe, Ingredients, Comment
from django_summernote.admin import SummernoteModelAdmin


class IngredientsInline(admin.TabularInline):
    model = Ingredients


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    inlines = [IngredientsInline, ]
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'author__email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Ingredients)
