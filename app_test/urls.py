from django.urls import path, include
from django.contrib import admin
from app_test.views import display_table

# index/hello...

urlpatterns = [
    path("", display_table, name="display_table"),
    path("api", include("app_api.urls")),

   # path("", include("app_test.urls")),/
]
