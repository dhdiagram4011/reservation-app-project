from django.contrib.auth.models import Board, BoardPosts, Comment, likeDislike 
from rest_framework import viewsets
from rest_framework import permissions
from boardsapi.serializers import BoardSerializer, BoardPostsSerializer, CommentSerializer, likeDislikeSerializer
## serializer = object to xml,json parse


class BoardViewsets(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardPostsViewsets(viewsets.ModelViewSet):
    queryset = BoardPosts.objects.all()
    serializer_class = BoardPostsSerializer


class CommentViewsets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class likeDislikeViewsets(viewsets.ModelViewSet):
    queryset = likeDislike.objects.all()
    serializer_class = likeDislikeSerializer