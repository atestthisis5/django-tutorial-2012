from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('hello_world.views',
    url(r'^(P<name>.[^/]+)/$', 'welcome', name='hello_world-welcome-name'),
    url(r'^(P<name>.[^/]+)/(?P<age>\d+)/$', 'welcome',
        name='hello_world-welcome-name-age'),

)