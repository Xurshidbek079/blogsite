from django.views.generic import ListView, DetailView, TemplateView
from .models import BlogPost

class HomeView(TemplateView):
    template_name = 'blog/home.html'

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class ChannelView(TemplateView):
    template_name = 'blog/channel.html'

class ProjectsView(TemplateView):
    template_name = 'blog/projects.html'

class BooksView(TemplateView):
    template_name = 'blog/books.html'

class NowView(TemplateView):
    template_name = 'blog/now.html'

class ToolsView(TemplateView):
    template_name = 'blog/tools.html' 