from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.core.paginator import Paginator
from itertools import groupby
from .models import (
    BlogPost, AboutSection, Project, Book, 
    NowActivity, Tool, ToolCategory
)


class HomePageView(TemplateView):
    template_name = 'blog/home.html'


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-written_date']
    
    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class AboutPageView(TemplateView):
    template_name = 'blog/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = AboutSection.objects.filter(is_active=True)
        return context


class ProjectsPageView(TemplateView):
    template_name = 'blog/projects.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(is_featured=True)
        context['all_projects'] = Project.objects.all()
        return context


class BooksPageView(TemplateView):
    template_name = 'blog/books.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currently_reading'] = Book.objects.filter(status='currently_reading')
        context['completed_books'] = Book.objects.filter(status='completed')
        context['want_to_read'] = Book.objects.filter(status='want_to_read')
        context['recommended_books'] = Book.objects.filter(is_recommended=True)
        return context


class NowPageView(TemplateView):
    template_name = 'blog/now.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_activities'] = NowActivity.objects.filter(is_active=True)
        return context


class ToolsPageView(TemplateView):
    template_name = 'blog/tools.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get tools ordered by category and then by order within category
        all_tools = Tool.objects.select_related('category').order_by('category__order', 'order')
        # Group tools by category
        context['tools_by_category'] = groupby(all_tools, key=lambda tool: tool.category)
        context['categories'] = ToolCategory.objects.all()
        context['favorite_tools'] = Tool.objects.filter(is_favorite=True)
        context['currently_using'] = Tool.objects.filter(is_currently_using=True)
        return context 