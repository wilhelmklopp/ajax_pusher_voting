from django.conf.urls import patterns, include, url
from django.contrib import admin
from voting import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pubsub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('voting.urls')),
    url(r'^new/', views.new_counter, name='new_counter'),
    url(r'^rv/', views.receive_votes, name='receive_votes'),
)
