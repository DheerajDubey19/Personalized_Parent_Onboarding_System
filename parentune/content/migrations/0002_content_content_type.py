# Generated by Django 4.2.5 on 2024-06-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='content_type',
            field=models.CharField(blank=True, choices=[('blog', 'Blog'), ('vlog', 'Vlog')], max_length=10, null=True),
        ),
    ]