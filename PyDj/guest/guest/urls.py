"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from sign import views  # 导入sign 应用 views文件


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),  # 添加 index/路径配置
    url(r'^$', views.index),
    url(r'^accounts/login/$', views.index),
    url(r'^login_action/$', views.login_action),    # 添加 登录login_action 路径配置
    url(r'^event_manage/$', views.event_manage),    # 添加 发布会管理 event_manage 路径配置
    url(r'^search_name/$', views.search_name),      # 添加 搜索search_name 路径配置
    url(r'^guest_manage/$', views.guest_manage),    # 添加 嘉宾管理 guest_manage 路径配置
    url(r'^search_rename/$', views.search_rename),      # 添加 搜索search_rename 路径配置
    url(r'^sign_index/(?P<eid>[0-9]+)/$', views.sign_index),     # 添加 sign_index 签到 路径配置
    url(r'^sign_index_action/(?P<eid>[0-9]+)/$', views.sign_index_action),  # 添加 sign_index_action 签到动作 路径配置
    url(r'^logout/$', views.logout),     # 添加 logout 退出路径配置
    url(r'^api/', include('sign.urls', namespace = 'sign')),


]
