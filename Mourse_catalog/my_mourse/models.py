from datetime import date

from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.urls import reverse

User = settings.AUTH_USER_MODEL

# Create your models here.


class Mourse(models.Model):
    title = models.CharField(max_length=25)
    # slug = models.SlugField(max_length=25, unique=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default="2021-12-25", null=True, blank=True)
    q_lectures = models.IntegerField(default=0)

    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
   
    # def get_absolute_url(self):
    #     return reverse('home')
    #
    # def get_edit_url(self):
    #     return reverse('home')
    #
    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         # "author": self.author,
    #         # "slug": self.slug,
    #         "title": self.title,
    #         "description": self.description,
    #         "start_date": self.start_date,
    #         "end_date": self.end_date,
    #         "q_lectures": self.q_lectures,
    #     }

# @receiver(pre_save, sender=Post)
# def pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#
#
# TODO: https://www.geeksforgeeks.org/add-the-slug-field-inside-django-model/
