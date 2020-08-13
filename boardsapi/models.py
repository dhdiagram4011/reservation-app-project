#boardsapi model

from django.db import models

TEND = (
    ('like', '좋아요'),
    ('dislike', '싫어요'),
)


class Boardman(models.Model): #게시판리스트
    board_name = models.CharField(max_length=1000)
    board_title = models.CharField(max_length=100)
    board_maker = models.CharField(max_length=10)

    def __str__(self):
        return self.board_title


class BoardPosts(models.Model):
    writer = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    document = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    boardtitle = models.ForeignKey('Boardman', related_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return self.boardtitle


class Comment(models.Model):
    parentComments = models.TextField(max_length=500)
    writer = models.CharField(max_length=10)
    document = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now=True)
    target_post = models.ForeignKey('BoardPosts', related_name='posttitle', on_delete=models.CASCADE)

    

class likeDislike(models.Model):
    writer = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now=True)
    #comment = models.ForeignKey('BoardPosts', related_name='writer', on_delete=models.CASCADE) #댓글
    #posts = models.ForeignKey('BoardPosts', related_name='writer', on_delete=models.CASCADE)  #게시글
    tendency = models.CharField(max_length=10, choices=TEND, default='좋아요/싫어요', null=True)   #좋아요,싫어요
