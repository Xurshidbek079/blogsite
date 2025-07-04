from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.core.paginator import Paginator
from itertools import groupby
from .models import (
    BlogPost, AboutSection, Project, Book, 
    NowActivity, ToolSection
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
        context['projects'] = Project.objects.all()
        return context


class BooksPageView(TemplateView):
    template_name = 'blog/books.html'


class BooksCompletedView(TemplateView):
    template_name = 'blog/books_completed.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['completed_books'] = Book.objects.filter(status='completed')
        return context


class BooksCurrentlyReadingView(TemplateView):
    template_name = 'blog/books_currently_reading.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currently_reading'] = Book.objects.filter(status='currently_reading')
        return context


class BooksWantToReadView(TemplateView):
    template_name = 'blog/books_want_to_read.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['want_to_read'] = Book.objects.filter(status='want_to_read')
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'blog/book_detail.html'
    context_object_name = 'book'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_queryset(self):
        return Book.objects.all()


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
        context['tool_sections'] = ToolSection.objects.all()
        # Get the latest update date across all sections
        latest_section = ToolSection.objects.order_by('-last_updated').first()
        context['last_updated'] = latest_section.last_updated if latest_section else None
        return context 