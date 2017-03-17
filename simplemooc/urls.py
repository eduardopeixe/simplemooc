from django.conf.urls import include, url

from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)
