from django.views.generic.list import ListView
from django.utils import timezone

# Create your views here.

from igor.about.models import Section, About
from igor.blog.models import Entry


class AboutListView(ListView):

    model = Section

    template_name = 'about.html'

    def get_context_data(self, **kwargs):
    	context = super(AboutListView, self).get_context_data(**kwargs)
    	try:
    		context['about'] = About.objects.all()[0]
    	except IndexError:
    		context['about'] = 'You can update this section in the admin.'
    	context['recent_posts'] = Entry.objects.all().order_by('-pub_date')[:5]
    #     context['now'] = timezone.now()
    	return context
