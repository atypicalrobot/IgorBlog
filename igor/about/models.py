from django.db import models


# Create your models here.
class Section(models.Model):
	name = models.CharField(max_length=255)
	body = models.CharField(max_length=255)
	icon = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class About(models.Model):
	body = models.TextField()
	picture = models.ImageField(upload_to='about/', blank=True, null=True)

	class Meta:
		verbose_name_plural = 'About'

	def __str__(self):
		return self.body[:100]
