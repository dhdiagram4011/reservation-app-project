#boardsapi model

from django.db import models

TEND = (
    ('like', '좋아요'),
    ('dislike', '싫어요'),
)


class Board(models.Model):
    writer = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    explanation = models.TextField(max_length=1000)


class BoardPosts(models.Model):
    writer = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    document = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    parentComments = models.TextField(max_length=500)
    writer = models.CharField(max_length=10)
    document = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now=True)
    boardPost = models.ForeignKey('BoardPosts', on_delete=models.CASCADE)


class likeDislike(models.Model):
    writer = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now=True)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE) #댓글
    posts = models.ForeignKey('BoardPosts', on_delete=models.CASCADE)  #게시글
    tendency = models.CharField(max_length=5, choices=TEND, default='좋아요/싫어요', null=True)   #좋아요,싫어요