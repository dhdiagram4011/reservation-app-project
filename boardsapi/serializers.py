#from django.contrib.auth.models import Board, BoardPosts, Comment, likeDislike
from .models import BoardPosts, Comment, likeDislike, Boardman
from rest_framework import routers, serializers



class BoardSerializer(serializers.HyperlinkedModelSerializer):
    #title = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Boardman
        fields = ['board_name','board_title','board_maker']


class BoardPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardPosts
        fields = ['writer','title','document','boardtitle','created_date']


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
    title = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Comment
        fields = ['parentComments','writer','document','title']



class likeDislikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = likeDislike
        fields = ['writer','created_date','comment','posts','tendency']



