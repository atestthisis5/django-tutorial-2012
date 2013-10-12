
def site_context(request):
    return {'company': 'My Company, Inc.',
            'user': request.user,
            'remote_ip': request.META['REMOTE_ADDR'],
            'logo': 'http://localhost:8000/img/logo.png'
    }

