# Generated by Django 4.2 on 2025-06-09 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpost_options_remove_blogpost_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='is_featured',
        ),
    ]
