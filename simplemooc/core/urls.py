from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contact/$', 'simplemooc.core.views.contact', name='contact'),
)
