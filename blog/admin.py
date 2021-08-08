from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'status')
    list_filter = ('published', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'published']

admin.site.register(Article, ArticleAdmin)
