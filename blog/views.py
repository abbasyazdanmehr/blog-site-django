from blog.models import Article, Category
from django.shortcuts import render, get_object_or_404

# Create your views here.


def home(request):
    context = {
        "articles": Article.objects.filter(status='p').order_by('published'),
        "categories": Category.objects.filter(status=True) # there is no need for .order_by because ordered in class Meta
    }
    return render(request, "blog/home.html", context)

def detail(request, slug):
    context = {
        "article": get_object_or_404(Article, slug=slug, status="p")
    }
    return render(request, "blog/detail.html", context)
