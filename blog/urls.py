from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('essays/', views.BlogListView.as_view(), name='blog_list'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('projects/', views.ProjectsPageView.as_view(), name='projects'),
    path('books/', views.BooksPageView.as_view(), name='books'),
    path('now/', views.NowPageView.as_view(), name='now'),
    path('tools/', views.ToolsPageView.as_view(), name='tools'),
    path('essays/<slug:slug>.html', views.PostDetailView.as_view(), name='post_detail'),
] 