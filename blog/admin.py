from django.contrib import admin
from .models import Article, Category

# Register your models here.

# Admin customization
admin.site.site_header = "هولولولولو"

# Actions
def make_published(modeladmin, request, queryset):
    rows_update = queryset.update(status='p')
    if rows_update == 1:
        message_bit = "منتشر شد"
    else:
        message_bit = "منتشر شدند" % rows_update
    modeladmin.message_user(request, "%s مقاله %s" % (rows_update, message_bit))
            
make_published.short_description = 'انتشار مقالات انتخابی'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}    
    
admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'author', 'j_published', 'status', 'category_to_str')
    list_filter = ('published', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'published']
    actions = [make_published]
    
    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = 'دسته بندی'

admin.site.register(Article, ArticleAdmin)
