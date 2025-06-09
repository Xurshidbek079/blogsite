from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField('Sarlavha', max_length=200)
    slug = models.SlugField('URL nomi', unique=True)
    content = models.TextField('Mazmun')
    created_at = models.DateTimeField('Yaratilgan vaqt', auto_now_add=True)
    updated_at = models.DateTimeField('Yangilangan vaqt', auto_now=True)
    is_published = models.BooleanField('Nashr etilgan', default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Maqola'
        verbose_name_plural = 'Blog Maqolalar'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})


# About Page Models
class AboutSection(models.Model):
    title = models.CharField('Sarlavha', max_length=200)
    content = models.TextField('Mazmun')
    image = models.ImageField('Rasm', upload_to='images/about/', blank=True, null=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)
    created_at = models.DateTimeField('Yaratilgan vaqt', auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Haqida Bo\'lim'
        verbose_name_plural = 'Haqida Bo\'limlari'

    def __str__(self):
        return self.title


# Projects Models
class ProjectCategory(models.Model):
    name = models.CharField('Nomi', max_length=100)
    slug = models.SlugField('URL nomi', unique=True)
    description = models.TextField('Tavsif', blank=True)

    class Meta:
        verbose_name = 'Loyiha Kategoriyasi'
        verbose_name_plural = 'Loyiha Kategoriyalari'

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('planning', 'Rejalashtirish'),
        ('in_progress', 'Jarayonda'),
        ('completed', 'Tugallangan'),
        ('on_hold', 'To\'xtatilgan'),
    ]

    title = models.CharField('Nomi', max_length=200)
    slug = models.SlugField('URL nomi', unique=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, verbose_name='Kategoriya')
    description = models.TextField('Tavsif')
    image = models.ImageField('Rasm', upload_to='images/projects/', blank=True, null=True)
    technologies = models.CharField('Texnologiyalar', max_length=300, help_text='Vergul bilan ajrating')
    demo_url = models.URLField('Demo URL', blank=True, null=True)
    github_url = models.URLField('GitHub URL', blank=True, null=True)
    status = models.CharField('Holat', max_length=20, choices=STATUS_CHOICES, default='completed')
    start_date = models.DateField('Boshlanish sanasi', blank=True, null=True)
    end_date = models.DateField('Tugash sanasi', blank=True, null=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_featured = models.BooleanField('Asosiy loyiha', default=False)
    created_at = models.DateTimeField('Yaratilgan vaqt', auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Loyiha'
        verbose_name_plural = 'Loyihalar'

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


# Books Models
class Book(models.Model):
    STATUS_CHOICES = [
        ('want_to_read', 'O\'qishni istyman'),
        ('currently_reading', 'Hozir o\'qiyapman'),
        ('completed', 'O\'qib tugatdim'),
        ('paused', 'To\'xtatdim'),
    ]

    RATING_CHOICES = [
        (1, '1 - Juda yomon'),
        (2, '2 - Yomon'),
        (3, '3 - O\'rtacha'),
        (4, '4 - Yaxshi'),
        (5, '5 - Zo\'r'),
    ]

    title = models.CharField('Kitob nomi', max_length=200)
    author = models.CharField('Muallif', max_length=200)
    cover_image = models.ImageField('Muqova', upload_to='images/books/', blank=True, null=True)
    status = models.CharField('Holat', max_length=20, choices=STATUS_CHOICES, default='want_to_read')
    rating = models.IntegerField('Baho', choices=RATING_CHOICES, blank=True, null=True)
    review = models.TextField('Sharh', blank=True)
    key_takeaways = models.TextField('Asosiy xulosalar', blank=True)
    start_date = models.DateField('Boshlanish sanasi', blank=True, null=True)
    finish_date = models.DateField('Tugash sanasi', blank=True, null=True)
    pages = models.PositiveIntegerField('Sahifalar soni', blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=20, blank=True)
    buy_url = models.URLField('Sotib olish URL', blank=True, null=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    is_recommended = models.BooleanField('Tavsiya etaman', default=False)
    created_at = models.DateTimeField('Yaratilgan vaqt', auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar'

    def __str__(self):
        return f"{self.title} - {self.author}"


# Now Page Models
class NowCategory(models.Model):
    name = models.CharField('Nomi', max_length=100)
    icon = models.CharField('Icon', max_length=50, blank=True, help_text='Font Awesome icon class')
    color = models.CharField('Rang', max_length=7, default='#000000', help_text='Hex rang kodi')
    order = models.PositiveIntegerField('Tartib', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Hozir Kategoriyasi'
        verbose_name_plural = 'Hozir Kategoriyalari'

    def __str__(self):
        return self.name


class NowActivity(models.Model):
    category = models.ForeignKey(NowCategory, on_delete=models.CASCADE, verbose_name='Kategoriya')
    title = models.CharField('Nomi', max_length=200)
    description = models.TextField('Tavsif')
    image = models.ImageField('Rasm', upload_to='images/now/', blank=True, null=True)
    url = models.URLField('Bog\'lanish URL', blank=True, null=True)
    start_date = models.DateField('Boshlanish sanasi')
    end_date = models.DateField('Tugash sanasi', blank=True, null=True)
    is_active = models.BooleanField('Faol', default=True)
    progress = models.PositiveIntegerField('Jarayon (%)', default=0, help_text='0-100 orasida')
    order = models.PositiveIntegerField('Tartib', default=0)
    created_at = models.DateTimeField('Yaratilgan vaqt', auto_now_add=True)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = 'Hozirgi Faoliyat'
        verbose_name_plural = 'Hozirgi Faoliyatlar'

    def __str__(self):
        return f"{self.title} ({self.category.name})"


# Tools Models
class ToolCategory(models.Model):
    name = models.CharField('Nomi', max_length=100)
    description = models.TextField('Tavsif', blank=True)
    icon = models.CharField('Icon', max_length=50, blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Vosita Kategoriyasi'
        verbose_name_plural = 'Vosita Kategoriyalari'

    def __str__(self):
        return self.name


class Tool(models.Model):
    PROFICIENCY_CHOICES = [
        ('beginner', 'Boshlang\'ich'),
        ('intermediate', 'O\'rta'),
        ('advanced', 'Yuqori'),
        ('expert', 'Mutaxassis'),
    ]

    name = models.CharField('Nomi', max_length=100)
    category = models.ForeignKey(ToolCategory, on_delete=models.CASCADE, verbose_name='Kategoriya')
    description = models.TextField('Tavsif')
    logo = models.ImageField('Logo', upload_to='images/tools/logos/', blank=True, null=True)
    website_url = models.URLField('Veb-sayt URL', blank=True, null=True)
    proficiency = models.CharField('Malaka darajasi', max_length=20, choices=PROFICIENCY_CHOICES)
    years_experience = models.DecimalField('Tajriba (yil)', max_digits=4, decimal_places=1, blank=True, null=True)
    is_favorite = models.BooleanField('Sevimli', default=False)
    is_currently_using = models.BooleanField('Hozir ishlataman', default=True)
    notes = models.TextField('Izohlar', blank=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    created_at = models.DateTimeField('Yaratilgan vaqt', auto_now_add=True)

    class Meta:
        ordering = ['category__order', 'order', 'name']
        verbose_name = 'Vosita'
        verbose_name_plural = 'Vositalar'

    def __str__(self):
        return f"{self.name} ({self.category.name})" 