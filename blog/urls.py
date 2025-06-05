from django.urls import path
from .views import (
    HomeView, BlogPostListView, BlogPostDetailView, 
    AboutView, ChannelView, ProjectsView, BooksView, NowView, ToolsView
)

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogPostListView.as_view(), name='blog_list'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('channel/', ChannelView.as_view(), name='channel'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('books/', BooksView.as_view(), name='books'),
    path('now/', NowView.as_view(), name='now'),
    path('tools/', ToolsView.as_view(), name='tools'),
] 