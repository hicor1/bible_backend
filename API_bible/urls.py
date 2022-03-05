from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'API_bible' #Namespace에 등록해야 {% url %}에서 call할수있다

router = DefaultRouter()

# 접근방법 : 예)  http://127.0.0.1:8000/API_bible/test/gettest/
router.register(r'test', views.rest_api_test, basename='test')


urlpatterns = [
    path('',include(router.urls)),
]