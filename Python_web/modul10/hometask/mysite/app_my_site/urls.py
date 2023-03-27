from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "app_my_site"

urlpatterns = [
    path("", views.main, name="root"),
    path("upload_author", views.upload_author, name="upload_author"),
    path("upload_quote", views.upload_quote, name="upload_quote"),
    path("author/<int:pk>", views.authors_descr, name="authors_descr"),
]
