from django.urls import path
from sign import views_if,views_if_sec

app_name = 'sign'
urlpatterns = [
    path('add_event/', views_if.add_event, name='add_event'),
    path('add_guest/', views_if.add_guest, name='add_guest'),
    path('get_event_list/', views_if.get_event_list, name = 'get_event_list'),
    path('get_guest_list/', views_if.get_guest_list, name = 'get_guest_list'),
    path('user_sign/', views_if.user_sign, name = 'user_sign'),

	path('sec_get_event_list/', views_if_sec.get_event_list, name='get_event_list'),
	path('sec_add_event/', views_if_sec.add_event, name='add_event'),
    path('sec_get_guest_list/', views_if_sec.get_guest_list, name='get_guest_list'),
    #path('sec_add_guest/', views_if_sec.add_guest, name='add_guest'),
	
	
    # url(r'^add_event/', views_if.add_event, name='add_event'),
    # url(r'^add_guest/', views_if.add_guest, name='add_guest'),
    # url(r'^get_event_list/', views_if.get_event_list, name = 'get_event_list'),
    # url(r'^get_guest_list/', views_if.get_guest_list, name = 'get_guest_list'),
    # url(r'^user_sign/', views_if.user_sign, name = 'user_sign'),
]