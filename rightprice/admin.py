# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from rightprice.models import Production, CarModel
admin.site.register(Production)
admin.site.register(CarModel)