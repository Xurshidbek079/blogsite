from django.contrib import admin
from .models import (
    BlogPost, AboutSection, ProjectCategory, Project, 
    Book, NowCategory, NowActivity, ToolCategory, Tool
)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'written_date', 'is_published']
    list_filter = ['is_published', 'written_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'written_date'


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
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'order', 'created_at']
    list_filter = ['category', 'status', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order', 'status']
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'description')
        }),
        ('Media and Links', {
            'fields': ('image', 'demo_url', 'github_url')
        }),
        ('Technical Details', {
            'fields': ('technologies', 'status', 'start_date', 'end_date')
        }),
        ('Display Settings', {
            'fields': ('order',)
        }),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'rating', 'order']
    list_filter = ['status', 'rating', 'created_at']
    search_fields = ['title', 'author', 'notes']
    list_editable = ['order', 'rating']
    readonly_fields = ['slug']
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'slug', 'author', 'cover_image', 'pages', 'isbn')
        }),
        ('Reading Status', {
            'fields': ('status', 'rating', 'start_date', 'finish_date')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
        ('Additional', {
            'fields': ('buy_url', 'order')
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
        ('Basic Information', {
            'fields': ('title', 'category', 'description')
        }),
        ('Media and Link', {
            'fields': ('image', 'url')
        }),
        ('Time and Status', {
            'fields': ('start_date', 'end_date', 'is_active', 'progress')
        }),
        ('Display', {
            'fields': ('order',)
        }),
    )


@admin.register(ToolCategory)
class ToolCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order']
    list_editable = ['order', 'icon']
    ordering = ['order']


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'years_experience', 'is_favorite', 'is_currently_using', 'order']
    list_filter = ['category', 'proficiency', 'is_favorite', 'is_currently_using']
    search_fields = ['name', 'description', 'notes']
    list_editable = ['order', 'is_favorite', 'is_currently_using']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'description')
        }),
        ('Media and Link', {
            'fields': ('logo', 'website_url')
        }),
        ('Experience', {
            'fields': ('proficiency', 'years_experience')
        }),
        ('Status', {
            'fields': ('is_favorite', 'is_currently_using')
        }),
        ('Additional', {
            'fields': ('notes', 'order')
        }),
    )


# Customize admin site header
admin.site.site_header = "Xurshid's Blog Admin"
admin.site.site_title = "Blog Admin"
admin.site.index_title = "Blog Admin Panel" 