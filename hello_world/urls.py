from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('hello_world.views',
    url(r'^(?P<name>.[^/]+)/$', 'welcome', name='hello_world-welcome-name'),
    url(r'^(?P<name>.[^/]+)/(?P<age>\d+)/$', 'welcome',
        name='hello_world-welcome-name-age'),
    url(r'^templateEx1$', 'template_ex1', name='hello_world-template_ex1'),
    url(r'^$', 'welcome', name='hello_world-welcome'),
)