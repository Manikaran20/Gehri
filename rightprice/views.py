# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'rightprice/index.html'
   
# Create your views here.
