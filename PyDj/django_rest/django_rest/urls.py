"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
from rest_framework import routers
from api import views



# Routers provide an easy way of automatically determiing the URL conf : 路由器提供了一种简单的方法来自动确定URL conf
router = routers.DefaultRouter()
router.register("users",  views.UserViewSet)
router.register("groups", views.GroupViewSet)
router.register("events", views.EventViewSet)
router.register("guests", views.GuestViewSet)

# Wire up our API using automatic URL routing : 使用自动URL路由连接我们的API
# Additionally, we include test_login URLs for the browsable API : 此外，我们还包括可浏览API的登录url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
