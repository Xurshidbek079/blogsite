from django.contrib import admin
from .models import (
    BlogPost, AboutSection, ProjectCategory, Project, 
    Book, NowCategory, NowActivity, ToolCategory, Tool
)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'is_published']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['order', 'is_active']
    ordering = ['order']


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'is_featured', 'order', 'created_at']
    list_filter = ['category', 'status', 'is_featured', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order', 'is_featured', 'status']
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Asosiy Ma\'lumotlar', {
            'fields': ('title', 'slug', 'category', 'description')
        }),
        ('Media va Havolalar', {
            'fields': ('image', 'demo_url', 'github_url')
        }),
        ('Texnik Ma\'lumotlar', {
            'fields': ('technologies', 'status', 'start_date', 'end_date')
        }),
        ('Ko\'rsatish Sozlamalari', {
            'fields': ('order', 'is_featured')
        }),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'rating', 'is_recommended', 'order']
    list_filter = ['status', 'rating', 'is_recommended', 'created_at']
    search_fields = ['title', 'author', 'review']
    list_editable = ['order', 'is_recommended', 'rating']
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Kitob Ma\'lumotlari', {
            'fields': ('title', 'author', 'cover_image', 'pages', 'isbn')
        }),
        ('O\'qish Holati', {
            'fields': ('status', 'rating', 'start_date', 'finish_date')
        }),
        ('Sharh va Xulosalar', {
            'fields': ('review', 'key_takeaways')
        }),
        ('Qo\'shimcha', {
            'fields': ('buy_url', 'order', 'is_recommended')
        }),
    )


@admin.register(NowCategory)
class NowCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'color', 'order']
    list_editable = ['order', 'icon', 'color']
    ordering = ['order']


@admin.register(NowActivity)
class NowActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'start_date', 'end_date', 'is_active', 'progress', 'order']
    list_filter = ['category', 'is_active', 'start_date']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active', 'progress']
    date_hierarchy = 'start_date'
    fieldsets = (
        ('Asosiy Ma\'lumotlar', {
            'fields': ('title', 'category', 'description')
        }),
        ('Media va Havola', {
            'fields': ('image', 'url')
        }),
        ('Vaqt va Holat', {
            'fields': ('start_date', 'end_date', 'is_active', 'progress')
        }),
        ('Ko\'rsatish', {
            'fields': ('order',)
        }),
    )


@admin.register(ToolCategory)
class ToolCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order']
    list_editable = ['order', 'icon']
    ordering = ['order']
    search_fields = ['name', 'description']


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'years_experience', 'is_favorite', 'is_currently_using', 'order']
    list_filter = ['category', 'proficiency', 'is_favorite', 'is_currently_using']
    search_fields = ['name', 'description', 'notes']
    list_editable = ['order', 'is_favorite', 'is_currently_using']
    fieldsets = (
        ('Asosiy Ma\'lumotlar', {
            'fields': ('name', 'category', 'description')
        }),
        ('Media va Havola', {
            'fields': ('logo', 'website_url')
        }),
        ('Tajriba', {
            'fields': ('proficiency', 'years_experience')
        }),
        ('Holat', {
            'fields': ('is_favorite', 'is_currently_using')
        }),
        ('Qo\'shimcha', {
            'fields': ('notes', 'order')
        }),
    )


# Customize admin site header
admin.site.site_header = "Xurshid's Blog Admin"
admin.site.site_title = "Blog Admin"
admin.site.index_title = "Blog Boshqaruv Paneli" 