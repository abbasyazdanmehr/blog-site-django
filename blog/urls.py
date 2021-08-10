from django.urls import path
from .views import category, home, detail

app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('article/<slug:slug>/', detail, name="detail"),
    path('category/<slug:slug>/', category, name="category"),
]

