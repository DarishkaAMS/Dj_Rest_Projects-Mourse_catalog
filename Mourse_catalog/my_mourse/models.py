from datetime import date

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# STATUS_CHOICES = (
#    ('draft', 'Draft'),
#    ('published', 'Published'),
# )


class Mourse(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    descr = models.TextField(max_length=255)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    q_lections = models.IntegerField(default=0)
#     status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default ='draft')

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
# TODO: https://www.geeksforgeeks.org/add-the-slug-field-inside-django-model/
