from django.db import models
from django.utils import timezone
from extensions.utils import jalali_convertor
from django.utils.html import format_html

# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, 
                               blank=True, on_delete=models.SET_NULL, 
                               related_name='children', verbose_name='زیردسته')
    title = models.CharField(max_length=30, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='شناسه')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='مکان/اولویت')
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']
        
    def __str__(self):
        return self.title

class Article(models.Model):
    
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    
    title = models.CharField(max_length=30, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='شناسه')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='articles')
    description = models.TextField(verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to="images", verbose_name='تصویر')
    published = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"
    
    def __str__(self):
        return self.title
    
    def j_published(self):
        return jalali_convertor(self.published) 
    
    def category_publish(self):
        return self.category.filter(status=True)
    
    def thumbnail_tag(self):
        return format_html("<img src='{}' height=45 width=80>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "عکس مقاله"
    