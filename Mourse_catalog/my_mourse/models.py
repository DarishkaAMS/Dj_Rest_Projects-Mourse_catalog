from datetime import date

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Mourse(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    descr = models.TextField(max_length=255)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    q_lections = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.author)