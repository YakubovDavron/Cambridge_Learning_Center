from rest_framework import serializers
from .models import About, Client, Team, Users, Video_lessons, Websites, Web_Images, Payment


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['is_pay']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ['region']


class Video_lessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_lessons
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']


class WebsitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Websites

        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']


class Web_ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web_Images
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment

        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
