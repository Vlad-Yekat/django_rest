from django.conf.urls import url
from django.urls import path, include

# from .views import MixPostDetailView
from .views import PostsList, PostsDetail, PostVer2List, PostVer2Detail
from . import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register('mixpostlist', views.MixPostListView)
# router.register('videolist', views.VideoView)
# router.register('audiolist', views.AudioView)
# router.register('textslist', views.TextsView)#

# urlpatterns = [
#    path('', include(router.urls))
# ]

urlpatterns = [
    url(r'^posts/$', PostsList.as_view(), name='posts-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostsDetail.as_view(), name='mixpost-detail'),
    url(r'^newver2/$', PostVer2List.as_view(), name='ver2-list'),
    url(r'^newver2/(?P<pk>[0-9]+)/$', PostVer2Detail.as_view(), name='postver2-detail'),
    url(r'^$', views.api_root),

]
