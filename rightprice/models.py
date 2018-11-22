# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Production(models.Model):
	brand = models.CharField(max_length = 199)
	pub_date = models.DateTimeField('datetime')
	def __str__(self):
		return self.brand

@python_2_unicode_compatible
class CarModel(models.Model):
	name = models.ForeignKey(Production, on_delete=models.CASCADE)
	model_choice = models.CharField(max_length=499)
	def __str__(self):
		return self.model_choice
