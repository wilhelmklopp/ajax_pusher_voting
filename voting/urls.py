from django.conf.urls import patterns, url

from voting import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )
