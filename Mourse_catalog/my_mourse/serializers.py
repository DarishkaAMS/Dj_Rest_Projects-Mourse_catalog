# from rest_framework import serializers
# 
# from .models import Mourse
# 
# 
# class MourseSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=25)
#     slug = serializers.SlugField(max_length=250, null=True, blank=True)
#     author = PublicProfileSerializer(source='user.profile', read_only=True)
#     description = serializers.TextField(max_length=255)
#     start_date = serializers.DateField(default=date.today)
#     end_date = serializers.DateField(default="2021-12-25", null=True, blank=True)
#     q_lectures = serializers.IntegerField(default=0)
#     
#     class Meta:
#         model = Mourse
#         fields = ('id', 'title', 'slug', 'author', 'description', 'start_date', 'end_date', 'q_lectures')
