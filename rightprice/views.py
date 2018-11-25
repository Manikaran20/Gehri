# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from rightprice.models import Production


class IndexView(generic.ListView):
    template_name = 'rightprice/index.html'
    context_object_name = 'latest_production_list'

    def get_queryset(self):
    	return Production.objects.order_by('pub_date')

def Car(request):
	latest_production_list = Production.objects.all()
	return render(request, 'rightprice/car.html', {'latest_production_list':latest_production_list})

def House(request):
	return render(request, 'rightprice/house.html')
	

