#데이터 처리
from gc import get_referents
from typing import Generic
from  .models import Blog
from .serializer import BlogSerializer

#APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

#Mixins
from rest_framework import generics
from rest_framework import mixins
    

class BlogList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset= Blog.objects.all()
    serializer_class=BlogSerializer

    # show blog list
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


    #create new post
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class BlogDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset= Blog.objects.all()
    serializer_class=BlogSerializer

    #show details
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    #update Blog
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    #delete Blog
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

        

