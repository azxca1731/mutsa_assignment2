from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pup_date = models.DateTimeField('date published')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    pup_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.comment
