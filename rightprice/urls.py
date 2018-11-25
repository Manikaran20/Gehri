from django.conf.urls import url
from . import views

app_name = 'rightprice'

urlpatterns = [
url(r'^$', views.IndexView.as_view(), name='index'),
url(r'^xyz$', views.Detail, name='detail'),

]