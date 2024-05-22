from rest_framework import generics
from .models import (Client,
                     Web_Images,
                     Websites,
                     About,
                     Team,
                     Payment,
                     Video_lessons,
                     Users)

from .seri import (ClientSerializer,
                   AboutSerializer,
                   Video_lessonsSerializer,
                   TeamSerializer,
                   WebsitesSerializer,
                   Web_ImagesSerializer,
                   PaymentSerializer,
                   UsersSerializer)


class ClientListApiView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class WebsiteApiView(generics.ListCreateAPIView):
    queryset = Websites.objects.all()
    serializer_class = WebsitesSerializer


class AboutApiview(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class Video_lessonsApiView(generics.ListCreateAPIView):
    queryset = Video_lessons.objects.all()
    serializer_class = Video_lessonsSerializer


class TeamApiView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class Web_ImagesApiView(generics.ListCreateAPIView):
    queryset = Web_Images.objects.all()
    serializer_class = Web_ImagesSerializer


class PaymentApiView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class UsersApiView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
