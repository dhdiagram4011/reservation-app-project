from django.urls import path, include
from rest_framework import routers
from boardsapi import views

app_name = "boardsapi"

router = routers.DefaultRouter()

router.register(r'board', views.BoardViewsets)
router.register(r'boardposts', views.BoardPostsViewsets)
router.register(r'comment', views.CommentViewsets)
router.register(r'likedislike', views.likeDislikeViewsets)

urlpatterns = [
    path('', include(router.urls)),
    path('boards-api/', include('rest_framework.urls')),

]