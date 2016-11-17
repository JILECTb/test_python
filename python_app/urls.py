from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from python_app import views

urlpatterns = [
    url(r'^devices/$', views.DeviceList.as_view()),
    url(r'^devices/(?P<pk>[0-9]+)/$', views.DeviceDetail.as_view()),
    url(r'^user_devices/$', views.UserDeviceList.as_view()),

    url(r'^readings/$', views.ReadingList.as_view()),
    url(r'^readings/(?P<pk>[0-9]+)/$', views.ReadingDetail.as_view()),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^$', views.UserDeviceList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]