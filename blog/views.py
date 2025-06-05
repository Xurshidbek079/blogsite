from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.core.paginator import Paginator
from .models import BlogPost


class HomePageView(TemplateView):
    template_name = 'blog/home.html'


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class AboutPageView(TemplateView):
    template_name = 'blog/about.html'


class ProjectsPageView(TemplateView):
    template_name = 'blog/projects.html'


class BooksPageView(TemplateView):
    template_name = 'blog/books.html'


class NowPageView(TemplateView):
    template_name = 'blog/now.html'


class ToolsPageView(TemplateView):
    template_name = 'blog/tools.html' 