from django.conf.urls import *

from igor.blog import views

urlpatterns = patterns('',
	url(r'^detail/(?P<pk>[0-9]+)/$', views.EntryDetailView.as_view(), name='entry-detail'),
    url(r'^(?P<year>\d{4})/(?P<month>[01]\d)/(?P<day>[0123]\d)/$', views.list_entries_by_date),
    url(r'^(?P<year>\d{4})/(?P<month>[01]\d)/$', views.list_entries_by_year_and_month),
    url(r'^(?P<year>\d{4})/$',     views.list_entries_by_year),
    url(r'^latest/$',              views.list_latest_entries),
    url(r'^today/$',               views.list_entries_for_today),
    url(r'^$',                     views.list_entries),
)
