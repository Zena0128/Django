from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Blog
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status


# #  전체 블로그 조회/한 블로그 생성. pk 필요 없는 동작들
# @api_view(['GET', 'POST'])  # 데코레이터
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def blog_list(request):
#     if request.method == 'GET':
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)  # 여러 데이터 직렬화하니까 many 써줘야 함!. 객체에서 딕셔너리로
#         return Response(serializer.data, status=status.HTTP_200_OK) # 딕셔너리에서 json으로
#     elif request.method == 'POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# class BlogList(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get(self, request):
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogList(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


####################


# # 한 블로그 조회/update/delete. pk 필요한 동작들
# @api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsOwnerOrReadOnly])
# def blog_detail(request, pk):
#     try:
#         blog = Blog.objects.get(pk=pk)
#         if request.method == 'GET':
#             serializer = BlogSerializer(blog)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         elif request.method == 'PUT':
#             serializer = BlogSerializer(blog, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(status=status.HTTP_200_OK)
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         elif request.method == 'DELETE':
#             blog.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     except Blog.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


# class BlogDetail(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsOwnerOrReadOnly]
#
#     def get_object(self, pk):
#         blog = get_object_or_404(Blog, pk=pk)
#         return blog
#
#     def get(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog, data=requeest.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         blog = self.get_object(pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]