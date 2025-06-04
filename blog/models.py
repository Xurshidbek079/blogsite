from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField(verbose_name="Matn")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqt")

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs) 