from django.http import HttpResponseNotFound

class AdminSubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]
        if request.path.startswith('/admin/') and host != 'admin.xurshidbro.uz':
            return HttpResponseNotFound('<h1>Sahifa topilmadi</h1>')
        return self.get_response(request) 