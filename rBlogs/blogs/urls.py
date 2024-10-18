from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('add/',views.add_blog, name="add_blog"),
    path("<int:blog_id>/edit",views.edit_blog,name="edit_blog"),
    path("<int:blog_id>/delete",views.delete_blog,name="delete_blog"),
    path("register/",views.registerUser,name="register"),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('search/', views.search_feature, name='search'),
]
