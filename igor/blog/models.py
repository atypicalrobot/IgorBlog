from django.core.urlresolvers import reverse
from django.db import models

from django_resized import ResizedImageField
from ckeditor.fields import RichTextField



from igor.blog.settings import TAGGING, TAGGIT, NANO_BLOG_TAGS

# Optional support for django-taggit
# For some unfathomable reason this cannot be imported inside the class
# as of Django 1.3
if NANO_BLOG_TAGS and NANO_BLOG_TAGS == TAGGIT:
    from taggit.managers import TaggableManager

class Entry(models.Model):
    headline = models.CharField(max_length=255, help_text='The first letter of each word will be automatically uppercased')
    content = RichTextField()
    pub_date = models.DateTimeField()
    picture = ResizedImageField(size=[1920, 1080], upload_to='blog/', blank=True, null=True, help_text='This field will scale any images larger than 1080p')

    # Optional support for django-taggit
    if NANO_BLOG_TAGS and NANO_BLOG_TAGS == TAGGIT:
        tags = TaggableManager(blank=True)

    class Meta:
        db_table = 'nano_blog_entry'
        verbose_name_plural = 'entries'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('entry-detail', args=[self.id])



# Optional support for django-tagging
if NANO_BLOG_TAGS and NANO_BLOG_TAGS == TAGGING:
    TAGGING.register(Entry)
