from django.db import models

# Message Sender Web Page
class MsgPush(models.Model):
    sender = models.CharField(max_length=11, default='010-000-0000')
    receiver = models.CharField(max_length=11, default='010-000-0000')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    


