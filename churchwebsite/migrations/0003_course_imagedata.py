# Generated by Django 4.1.7 on 2023-09-13 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchwebsite', '0002_churchuser_location_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=120, verbose_name='Course Name')),
                ('web_link', models.URLField(blank=True, verbose_name='Website Address')),
                ('grade', models.CharField(max_length=40, verbose_name='Grade')),
                ('description', models.TextField(blank=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='course/')),
            ],
        ),
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField(blank=True, max_length=255)),
                ('web_link', models.URLField(blank=True, verbose_name='Website Address')),
                ('image', models.ImageField(null=True, upload_to='img/')),
                ('path', models.TextField(blank=True, max_length=120)),
            ],
        ),
    ]
