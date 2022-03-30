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

from .utils import DB ## 직접 작성한 모듈 불러오기

# Create your views here.
@permission_classes((IsAuthenticated, )) # 권한을 체크합니다. 여기서는 로그인 했는지 여부만 체크하도록 하였습니다.
@authentication_classes((JSONWebTokenAuthentication,)) # JWT 토큰을 확인합니다. 토큰이 이상이 있으면 에러를 JSON 형식으로 반환합니다.
class rest_api_test(ModelViewSet):
    @action(detail=False, methods=['POST'])
    def gettest(self, request, format = None):
        
        #데이터 작업 수행
        data = DB.GetBibleBookList()['df']
        
        ########아래는 Dataframe데이터를 Json으로 바꿔줌, 매우중요!!#########
        result = data.to_dict(orient="records") #split
        
        # 데이터 정리
        content = {"data":result,
                   }
        
        # 리턴
        return Response(content)
