from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('all-articles/', views.articles, name='all_articles'),
    path('article/<slug:slug>/', views.open_article, name='this_article'),
]