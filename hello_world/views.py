# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden

def welcome(request, name=None, age=None):
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
