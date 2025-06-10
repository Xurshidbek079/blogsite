from django.http import Http404
from django.conf import settings

class AdminSubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]
        
        # Check if we're on the admin subdomain
        if host == 'admin.xurshidbro.uz':
            # Only allow /admin/ path
            if not request.path.startswith('/admin/'):
                raise Http404()
                
        return self.get_response(request) 