#from django.contrib.auth.models import Board, BoardPosts, Comment, likeDislike 
from .models import BoardPosts, Comment, likeDislike

from rest_framework import viewsets
from rest_framework import permissions
from boardsapi.serializers import BoardPostsSerializer, CommentSerializer, likeDislikeSerializer
## serializer = object to xml,json parse


# class BoardViewsets(viewsets.ModelViewSet): #전체 글 보기
#     queryset = Boardman.objects.all()
#     serializer_class = BoardSerializer


class BoardPostsViewsets(viewsets.ModelViewSet): #글쓰기
    queryset = BoardPosts.objects.all()
    serializer_class = BoardPostsSerializer


##전체 글 보기
class BoardPostsAllViewsets(viewsets.ModelViewSet):
    queryset = BoardPosts.objects.all()
    serializers_class = BoardPostsSerializer



class BoardDetailsViewsets(viewsets.ModelViewSet): #글 상세보기
    queryset = BoardPosts.objects.filter().values('id')
    serializer_class = BoardPostsSerializer  


class CommentViewsets(viewsets.ModelViewSet): #코멘트 달기
    queryset = Comment.objects.all()
    #queryset = BoardPosts.objects.all()
    serializer_class = CommentSerializer


class likeDislikeViewsets(viewsets.ModelViewSet): #좋아요/싫어요
    queryset = likeDislike.objects.all()
    serializer_class = likeDislikeSerializer