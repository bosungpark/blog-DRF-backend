from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

blog_list= views.BlogViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

blog_detail= views.BlogViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns=[
    path('blog/', blog_list),
    path('blog/<int:pk>/', blog_detail),
]

urlpatterns=format_suffix_patterns(urlpatterns)