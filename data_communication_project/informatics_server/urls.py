from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="informatics-home"),
    path('forums/', views.forums,name="informatics-forums"),
    path('repository/', views.repository,name="informatics-repository"),
    path('blog/', views.blog,name="informatics-blog"),
    path('managesite/', views.managesite,name="informatics-managesite"),
]