from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, EventSerializer, GuestSerializer
from api.models import Event, Guest


# Create your views here.

# ViewSets 定义视图的展现形式
class UserViewSet(viewsets.ModelViewSet):
    ''' 允许用户查看或编辑的API端点 '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    ''' 允许组查看或编辑的API端点 '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EventViewSet(viewsets.ModelViewSet):
    ''' API endpoint that allows events to be viewed or edited : 允许Event查看或编辑API端点 '''
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class GuestViewSet(viewsets.ModelViewSet):
    ''' API endpoint that allows guests to be viewed or edited : 允许Guest查看或编辑API端点 '''
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer