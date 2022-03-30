# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.views.static import serve
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


urlpatterns = [
    path('admin/',          admin.site.urls),
    path('API_test/',       include('API_test.urls')), ## App url 등록
    path('API_bible/',       include('API_bible.urls')), ## App url 등록

    # Django Rest framework JWT을 위한 URL 설정
    path('api/token/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
]