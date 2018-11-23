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
   

