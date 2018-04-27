from django.contrib.auth.models import User, Group
from rest_framework import  serializers
from api.models import Event, Guest

# 用户数据序列化
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

# 组别数据序列化
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

# 发布会数据序列化
class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'name', 'address', 'start_time', 'limit', 'status')

# 发布会用户数据序列化
class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ('url', 'realname', 'phone', 'email', 'sign', 'event')
