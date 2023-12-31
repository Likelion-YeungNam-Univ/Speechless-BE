# drf 관련 라이브러리
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, exceptions, status
from rest_framework.response import Response
from rest_framework.decorators import action

# drf 권한 관련 라이브러리
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# models.py
from .models import Estimate, Bookmark
# serializers.py
from .serializers import EstimateDetailSerializer, EstimateListSerializer, EstimateCreateSerializer, OfferListSerializer

class EstimateViewSet(viewsets.ModelViewSet):
    queryset = Estimate.objects.all()
    permission_classes_by_action = {
        'create': [IsAuthenticated],
        'retrieve': [AllowAny],
        'update': [IsAuthenticated],
        'list': [AllowAny],
        'destroy': [IsAuthenticated],
    }
                                    
    def get_serializer_class(self):
        if self.action == 'create':
            return EstimateCreateSerializer
        elif self.action == 'retrieve':
            return EstimateDetailSerializer
        elif self.action == 'update' :
            return EstimateDetailSerializer
        elif self.action == 'list' :
            return EstimateListSerializer
        elif self.action == 'destroy' :
            return EstimateListSerializer
        elif self.action == 'partial_update' :
            return EstimateDetailSerializer
        else :
            # 잘못된 요청임을 알리는 예외 발생
            raise exceptions.MethodNotAllowed(self.request.method)
        
    def create(self, request, *args, **kwargs):
        print("이거데이터임",request.data)
        return super().create(request, *args, **kwargs) 

    def update(self, request, *args, **kwargs):
        user = request.user
        if request.user != None:
            # jwt토큰 payload에 있는 user_id가 self object의 user_info 필드의 user_id와 같은지 비교.
            if user.user_id == int(kwargs['pk']):
                return super().update(request, *args, **kwargs)
            else :
                raise exceptions.PermissionDenied('수정 권한이 없습니다.')
        else :
            raise exceptions.PermissionDenied('로그인이 필요합니다.')   

    def destroy(self, request, *args, **kwargs):
        user = request.user
        if request.user != None:
            # jwt토큰 payload에 있는 user_id가 self object의 user_info 필드의 user_id와 같은지 비교.
            if user.user_id == int(kwargs['pk']):
                return super().destroy(request, *args, **kwargs)
            else :
                raise exceptions.PermissionDenied('삭제 권한이 없습니다.')
        else :
            raise exceptions.PermissionDenied('로그인이 필요합니다.')
                
    
# class BookmarkView(APIView):
#     def get(self, request):
#         permission_classes = [IsAuthenticated]
#         bookmarks = Bookmark.objects.filter()
#         serializer = BookmarkSerializer(bookmarks, many=True)
#         return Response(serializer.data)

