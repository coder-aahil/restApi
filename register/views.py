from django.shortcuts import render
from rest_framework import generics
from  register.models import Client,Project
from register.serializers import ClientSerializer,ProjectSerializer

# Create your views here.
class ClientList(generics.ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Client
    serializer_class=ProjectSerializer
class ProjectList(generics.ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Project
    serializer_class=ProjectSerializer
