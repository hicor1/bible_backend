from rest_framework.views import APIView # 장고 Apiview -> 상속받아 사용한다.
from rest_framework import serializers # post저장방식에서 사용한다
from rest_framework.response import Response
from django.shortcuts import render
from django_pandas.io import read_frame
from django.db.models import Q 
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
import json

from rest_framework import generics
from rest_framework.views import APIView 
from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

#from .module import * ## 직접 작성한 모듈 불러오기

# Create your views here.
class rest_api_test(ModelViewSet):
    
    @action(detail=False, methods=['GET'])
    def gettest(self, request, format = None):
        
        #데이터 작업 수행
        
        ########아래는 Dataframe데이터를 Json으로 바꿔줌, 매우중요!!#########
        #data_finish = data.to_dict(orient="record") #split
        # 샘플데이터
        data_finish = {"1":"test1", "2":"test2"}
        
        # 데이터 정리
        content = {"data":data_finish,
                   }
        
        # 리턴
        return Response(content)
