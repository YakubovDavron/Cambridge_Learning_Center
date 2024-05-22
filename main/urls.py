from django.urls import path
from .views import *

urlpatterns = [
    path('', AboutApiview.as_view(), name='about'),
    path('users/', UsersApiView.as_view(), name='users'),
    path('client/', ClientListApiView.as_view(), name='client'),
    path('payment/', PaymentApiView.as_view(), name='payment'),
    path('team/', TeamApiView.as_view(), name='team'),
    path('web_images/', Web_ImagesApiView.as_view(), name='web_images'),
    path('video_lessons/', Video_lessonsApiView.as_view(), name='video_lessons'),
]
