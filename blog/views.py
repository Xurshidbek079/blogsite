from django.views.generic import ListView, DetailView
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 10

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug' 