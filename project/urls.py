# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/',          admin.site.urls),
    path('API_test/',       include('API_test.urls')), ## App url 등록
    path('API_bible/',       include('API_bible.urls')), ## App url 등록
]