from django.urls import path,include
from pkg_resources import PkgResourcesDeprecationWarning
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

# blog_list= views.BlogViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# blog_detail= views.BlogViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'delete': 'destroy'
# })

router= DefaultRouter()
#blog
router.register('blog',BlogViewSet,basename='blog')
#comment
router.register('comment',CommentViewSet,basename='comment')

urlpatterns=[
    path('', include(router.urls)),
]

# urlpatterns=format_suffix_patterns(urlpatterns)