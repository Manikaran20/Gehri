from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'rightprice'

urlpatterns = [
url(r'^$', views.IndexView.as_view(), name='index'),
url(r'^Car$', views.Car, name='Car'),
url(r'^House$', views.House, name='House'),
url(r'^login/$', login, {'template_name': 'rightprice/login.html'} )
]