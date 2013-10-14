# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime
from hello_world import forms

def welcome_v1(request, name=None, age=None):
    if name:
        # The URL pattern matches only numbers, so we're not handling the 
        # ValueError that might happen if age isn't a numeric value.
        if not age or int(age) < 18:
            return HttpResponseForbidden('Grow up!')
        
        response=HttpResponse()
        
        # Here we treat the response as a file-like object.
        response.write('Hi %s, are you %s?' % (name, age, ))

        # Here we just set a siller header (though a valid HTTP header
        # would be just as applicable!)
        response['X-python-header']='That parrot is definitely dead.'
        return response
    else:
        # Here we pass it a string
        return HttpResponse('Hello!')
        # Here we pass it a generator (just as an example)
        # return HttpResponse(('<br>%d' % (i) for i in xrange(1,1000)))


def template_ex1(request):
    context = {'month' : 'Jan',
                'day' : 'Tuesday',
                'people': ['JOE','Mark','Alan'],
                'time' : datetime.today(),
                'names' : {'Jones': 'Alan',
                            'Anderson' : 'Jim',
                            'Smith': 'Jonas'},
                'autoescapedemo' : '''
{% if (time.minute % 2 == 0) %}
<p>The current minute {{ time.minute }} is even</p>
{% else %}
<p>The current minute {{ time.minute }} is odd</p>
{% endif %}
                ''',
                }
    return render_to_response('template_ex1.html', context)


def welcome(request, name=None, age=None):
    context = {'age' : age,
            'name': name,
    }

    return render_to_response('welcome.html', context, context_instance=RequestContext(request))

def session_ex(request):
    if request.session.get('counter', False) is False:
        request.session['counter'] = 0
        state = 'created'
        visits = request.session['counter']
    elif request.session['counter'] >= 10:
        del request.session['counter']
        state = 'deleted'
        visits = 'NaN'
    else:
        request.session['counter']+=1
        state = 'incremented'
        visits = request.session['counter']

    return render_to_response('session_ex.html',
        {'pagetitle': 'Django Session Counter',
         'visits': visits,
         'state': state, }
        )

def forms_ex(request):
    result = ''
    if request.POST.has_key('name'):
        form = forms.EventsForm(request.POST)
        if form.is_valid():
            m = form.save()
            print m.name
            form = forms.EventsForm()
            result = 'Saved data with PK of %s' % (m.pk,)
    else:
        form = forms.EventsForm()    
    
    c = {
        'form': form,
        'result': result,
    }

    return render_to_response('forms_ex.html', c, context_instance=RequestContext(request))

def forms_ex2(request):
    result = ''
    if request.POST.has_key('fname'):
        form = forms.PeopleForm(request.POST)
        if form.is_valid():
            m = form.save()
            print m.fname
            form = forms.PeopleForm()
            result = 'Saved data with PK of %s' % (m.pk,)
    else:
        form = forms.PeopleForm()

    c = {
        'form': form,
        'result': result,
    }

    return render_to_response('forms_ex2.html', c, context_instance=RequestContext(request))
