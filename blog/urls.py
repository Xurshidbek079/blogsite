from django.urls import path
from .views import BlogPostListView, BlogPostDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogPostListView.as_view(), name='home'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='post_detail'),
] 