#from django.contrib.auth.models import Board, BoardPosts, Comment, likeDislike
from .models import Board, BoardPosts, Comment, likeDislike
from rest_framework import routers, serializers



class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['writer','title','explanation']


class BoardPostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoardPosts
        fields = ['writer','title','document','created_date']


class BoardDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoardPosts
        fields = ['writer','title','document','created_date']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['parentComments','writer','document','created_date','boardPost']


class likeDislikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = likeDislike
        fields = ['writer','created_date','comment','posts','tendency']



