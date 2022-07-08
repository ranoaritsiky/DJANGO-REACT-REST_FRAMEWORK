from django.shortcuts import render

# rest_framework
from rest_framework import viewsets

# serializers
from .serializers import TodoSerializers

from .models import Todo

class TodoViewSets(viewsets.ModelViewSet):
    serializer_class=TodoSerializers
    queryset=Todo.objects.all()
