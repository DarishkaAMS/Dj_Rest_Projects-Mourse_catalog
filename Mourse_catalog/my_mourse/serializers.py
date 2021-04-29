# from rest_framework import serializers
#
# from .models import Mourse
#
#
# class MourseListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Mourse
#         fields = ('id', 'author', 'descr', 'start_date', 'q_lections')
#
#
# class MourseDetaisSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Mourse
#         fields = '__all__'
