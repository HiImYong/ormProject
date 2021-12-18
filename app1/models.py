from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()
