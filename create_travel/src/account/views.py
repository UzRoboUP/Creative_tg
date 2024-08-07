from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers
from . import models


import logging

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.MyTokenObtainPairSerializer
    queryset=models.User.objects.all()

class RegisterView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer


class UserSubscriptionCreateView(generics.CreateAPIView):
    queryset=models.User.objects.all()
    serializer_class=serializers.UserSubscribetionSerializer

class RetrieveUserDataView(generics.RetrieveAPIView):
    queryset=models.User.objects.all()
    serializer_class=serializers.UserRetrieveDataSerializer