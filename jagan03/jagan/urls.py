from django.conf.urls import patterns, url
from jagan import views

urlpatterns = patterns('',
                       url(r'^$', views.about, name='about'),
                       url(r'^timeline/$', views.timeline, name='timeline'),
                       )

