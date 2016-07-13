
from django.db import models



# Create your models here.
class Publication(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True, help_text='The first letter of each word will be automatically uppercased')
	abstract = models.TextField(blank=True, null=True)
	published_date = models.DateField(blank=True, null=True)
	link = models.URLField(blank=True, null=True)
	
	class Meta:
		verbose_name_plural = 'Publications'

	def __str__(self):
		return self.title
