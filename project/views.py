#데이터 처리
from  .models import Blog, Comment
from .serializer import BlogSerializer, CommentSerializer

# #APIView
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import Http404

# #Mixins
# from rest_framework import generics
# from rest_framework import mixins

#Generic CBV
from rest_framework import generics

#viewSet
from rest_framework import viewsets

#about athentications
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

class BlogViewSet(viewsets.ModelViewSet):

    authentication_classes=[BasicAuthentication,SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset= Blog.objects.all()
    serializer_class=BlogSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

# class BlogList(generics.ListCreateAPIView):

#     queryset= Blog.objects.all()
#     serializer_class=BlogSerializer

    # # show blog list
    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs)


    # #create new post
    # def post(self,request,*args,**kwargs):
    #     return self.create(request,*args,**kwargs)

# class BlogDetail(generics.RetrieveUpdateDestroyAPIView):

#     queryset= Blog.objects.all()
#     serializer_class=BlogSerializer

    # #show details
    # def get(self,request,*args,**kwargs):
    #     return self.retrieve(request,*args,**kwargs)

    # #update Blog
    # def put(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)

    # #delete Blog
    # def delete(self,request,*args,**kwargs):
    #     return self.destroy(request,*args,**kwargs)

class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes=[BasicAuthentication,SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)

