#from django.contrib.auth.models import Board, BoardPosts, Comment, likeDislike
from .models import Board, BoardPosts, Comment, likeDislike
from rest_framework import routers, serializers



class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['title']


class BoardPostsSerializer(serializers.HyperlinkedModelSerializer):
    boardtitle = serializers.StringRelatedField(many=True)

    class Meta:
        model = BoardPosts
        fields = ['writer','title','document','created_date','boardtitle']


class BoardPostsAllSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoardPosts
        fields = ['writer','title','document','created_date']
        read_only_fields = ['writer','title','document','created_date']



class BoardDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoardPosts
        fields = ['writer','title','document','created_date']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    ###title = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Comment
        fields = ['parentComments','writer','title','document','boardposts']


class likeDislikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = likeDislike
        fields = ['writer','created_date','comment','posts','tendency']


