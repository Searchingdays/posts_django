from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class msg(models.Model):
    msg_text = models.CharField(max_length=100)
    msg_date = models.DateTimeField("date of post")
    msg_like = models.IntegerField(default=0)
    msg_title = models.CharField(max_length=20)
    msg_know_more = models.BooleanField(default=False)

    def __str__(self):
        return self.msg_title
    
    #def what(self):
     #   return self.msg_date

class comment(models.Model):
    comment_text = models.CharField(max_length=1000)
    post = models.ForeignKey(msg, on_delete=models.CASCADE, default=None) # one comment can be connected to only 1 post. but 1 post may have many comments
    #comment_date = models.DateField("comment date", default=timezone.now())

    def __str__(self):
        return self.comment_text
    




# Create your models here.
