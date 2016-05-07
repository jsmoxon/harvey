from __future__ import unicode_literals

from django.db import models

class Agency(models.Model):
	agency_name = models.CharField(max_length=200, null=True, blank=True)
	fed_tax_ID = models.IntegerField(null=True, blank=True)
	address_line_one = models.CharField(max_length=2000, null=True, blank=True)
	address_line_two = models.CharField(max_length=2000, null=True, blank=True)
	address_city = models.CharField(max_length=2000, null=True, blank=True)
	address_state = models.CharField(max_length=2000, null=True, blank=True)
	address_zip = models.IntegerField(null=True, blank=True)
	

