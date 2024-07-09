from django.urls import path, include
from django.contrib import admin

from app_api.views import test_api, T_Api, P_Api
from app_test.views import display_table

# index/hello...

urlpatterns = [
    path("", T_Api.as_view()),
    path("/post/", P_Api.as_view()),

]
