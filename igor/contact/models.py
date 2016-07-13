from django.db import models


# Create your models here.
class Address(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	pobox = models.CharField(max_length=255, blank=True, null=True)
	street = models.CharField(max_length=255, blank=True, null=True)
	locality = models.CharField(max_length=255)
	postcode = models.CharField(max_length=25)
	country = models.CharField(max_length=255)

	class Meta:
		verbose_name_plural = 'Address'

	def __str__(self):
		return '{} {}'.format(self.name, self.locality)

