from django.db import models
from django.urls import reverse
from datetime import date


class BlogPost(models.Model):
    title = models.CharField('Title', max_length=200)
    slug = models.SlugField('URL slug', unique=True)
    content = models.TextField('Content')
    written_date = models.DateField('Written date', default=date.today, help_text='Date when the essay was written')
    is_published = models.BooleanField('Published', default=True)

    class Meta:
        ordering = ['-written_date']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})


# About Page Models
class AboutSection(models.Model):
    title = models.CharField('Title', max_length=200)
    content = models.TextField('Content')
    image = models.ImageField('Image', upload_to='images/about/', blank=True, null=True)
    order = models.PositiveIntegerField('Order', default=0)
    is_active = models.BooleanField('Active', default=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'About Section'
        verbose_name_plural = 'About Sections'

    def __str__(self):
        return self.title


# Projects Models
class ProjectCategory(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('URL slug', unique=True)
    description = models.TextField('Description', blank=True)

    class Meta:
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ]

    title = models.CharField('Title', max_length=200)
    slug = models.SlugField('URL slug', unique=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, verbose_name='Category')
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='images/projects/', blank=True, null=True)
    technologies = models.CharField('Technologies', max_length=300, help_text='Separate with commas')
    demo_url = models.URLField('Demo URL', blank=True, null=True)
    github_url = models.URLField('GitHub URL', blank=True, null=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='completed')
    start_date = models.DateField('Start date', blank=True, null=True)
    end_date = models.DateField('End date', blank=True, null=True)
    order = models.PositiveIntegerField('Order', default=0)
    is_featured = models.BooleanField('Featured project', default=False)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


# Books Models
class Book(models.Model):
    STATUS_CHOICES = [
        ('want_to_read', 'Want to Read'),
        ('currently_reading', 'Currently Reading'),
        ('completed', 'Completed'),
        ('paused', 'Paused'),
    ]

    RATING_CHOICES = [
        (1, '1 - Terrible'),
        (2, '2 - Bad'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]

    title = models.CharField('Book title', max_length=200)
    author = models.CharField('Author', max_length=200)
    cover_image = models.ImageField('Cover image', upload_to='images/books/', blank=True, null=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='want_to_read')
    rating = models.IntegerField('Rating', choices=RATING_CHOICES, blank=True, null=True)
    review = models.TextField('Review', blank=True)
    key_takeaways = models.TextField('Key takeaways', blank=True)
    start_date = models.DateField('Start date', blank=True, null=True)
    finish_date = models.DateField('Finish date', blank=True, null=True)
    pages = models.PositiveIntegerField('Page count', blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=20, blank=True)
    buy_url = models.URLField('Purchase URL', blank=True, null=True)
    order = models.PositiveIntegerField('Order', default=0)
    is_recommended = models.BooleanField('Recommended', default=False)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f"{self.title} - {self.author}"


# Now Page Models
class NowCategory(models.Model):
    name = models.CharField('Name', max_length=100)
    icon = models.CharField('Icon', max_length=50, blank=True, help_text='Font Awesome icon class')
    color = models.CharField('Color', max_length=7, default='#000000', help_text='Hex color code')
    order = models.PositiveIntegerField('Order', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Now Category'
        verbose_name_plural = 'Now Categories'

    def __str__(self):
        return self.name


class NowActivity(models.Model):
    category = models.ForeignKey(NowCategory, on_delete=models.CASCADE, verbose_name='Category')
    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='images/now/', blank=True, null=True)
    url = models.URLField('Related URL', blank=True, null=True)
    start_date = models.DateField('Start date')
    end_date = models.DateField('End date', blank=True, null=True)
    is_active = models.BooleanField('Active', default=True)
    progress = models.PositiveIntegerField('Progress (%)', default=0, help_text='Progress from 0-100')
    order = models.PositiveIntegerField('Order', default=0)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = 'Current Activity'
        verbose_name_plural = 'Current Activities'

    def __str__(self):
        return f"{self.title} ({self.category.name})"


# Tools Models
class ToolCategory(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', blank=True)
    icon = models.CharField('Icon', max_length=50, blank=True)
    order = models.PositiveIntegerField('Order', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Tool Category'
        verbose_name_plural = 'Tool Categories'

    def __str__(self):
        return self.name


class Tool(models.Model):
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    name = models.CharField('Name', max_length=100)
    category = models.ForeignKey(ToolCategory, on_delete=models.CASCADE, verbose_name='Category')
    description = models.TextField('Description')
    logo = models.ImageField('Logo', upload_to='images/tools/logos/', blank=True, null=True)
    website_url = models.URLField('Website URL', blank=True, null=True)
    proficiency = models.CharField('Proficiency level', max_length=20, choices=PROFICIENCY_CHOICES)
    years_experience = models.DecimalField('Years of experience', max_digits=4, decimal_places=1, blank=True, null=True)
    is_favorite = models.BooleanField('Favorite', default=False)
    is_currently_using = models.BooleanField('Currently using', default=True)
    notes = models.TextField('Notes', blank=True)
    order = models.PositiveIntegerField('Order', default=0)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        ordering = ['category__order', 'order', 'name']
        verbose_name = 'Tool'
        verbose_name_plural = 'Tools'

    def __str__(self):
        return f"{self.name} ({self.category.name})" 