from django.db import models


class BlogPost(models.Model):
    '''
    数据库，主键自动增加，默认带着
    '''
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp',)