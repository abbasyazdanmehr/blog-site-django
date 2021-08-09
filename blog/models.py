from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    
    title = models.CharField(max_length=30, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='شناسه')
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
    
    