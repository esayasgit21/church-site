# Generated by Django 4.1.7 on 2023-12-28 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('churchwebsite', '0003_churchuser_course_location_and_more'),
    ]

    operations = [
        
        migrations.DeleteModel(
            name='ImageData2',
        ),
    ]
