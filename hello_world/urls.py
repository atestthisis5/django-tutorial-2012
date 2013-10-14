from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('hello_world.views',
    url(r'^(?P<name>.[^/]+)/$', 'welcome', name='hello_world-welcome-name'),
    url(r'^(?P<name>.[^/]+)/(?P<age>\d+)/$', 'welcome',
        name='hello_world-welcome-name-age'),
    url(r'^templateEx1$', 'template_ex1', name='hello_world-template_ex1'),
    url(r'^sessionEx$', 'session_ex', name='hello_world-session_ex'),
    url(r'^formsEx$', 'forms_ex', name='hello_world-forms_ex'),
    url(r'^formsEx2$', 'forms_ex2', name='hello_world-forms_ex2'),
    url(r'^$', 'welcome', name='hello_world-welcome'),
)