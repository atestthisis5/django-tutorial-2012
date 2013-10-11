from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^(P<name>.[^/]+)/$', 'hello_world.views.welcome', name='hello_world-welcome-name'),
    url(r'^(P<name>.[^/]+)/(?P<age>\d+)/$', 'hello_world.views.welcome',
        name='hello_world-welcome-name-age'),
)