from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

# Create your views here.
# def main(resquest):
#     return HttpResponse('<h1>Hello-World</h1>')

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
