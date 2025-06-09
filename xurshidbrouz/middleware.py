from django.http import HttpResponseNotFound

class AdminSubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]
        # Allow admin access from admin subdomain and localhost for development
        allowed_admin_hosts = ['admin.xurshidbro.uz', 'localhost', '127.0.0.1']
        if request.path.startswith('/admin/') and host not in allowed_admin_hosts:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        return self.get_response(request) 