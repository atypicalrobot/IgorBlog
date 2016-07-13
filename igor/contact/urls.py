from django.conf.urls import patterns, url
from igor.contact import views

urlpatterns = patterns(
    '',
    url(r'^email/$',
        views.email,
        name='email'
        ),
    url(r'^thanks/$',
        views.thanks,
        name='thanks'
        ),
)