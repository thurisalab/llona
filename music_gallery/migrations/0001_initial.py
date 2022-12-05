# Generated by Django 3.2 on 2022-12-04 23:57

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('artist', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='MusicGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('ft', models.CharField(blank=True, max_length=1000, null=True)),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('note', models.TextField(max_length=1000)),
                ('music', cloudinary.models.CloudinaryField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music_gallery.album')),
            ],
            options={
                'verbose_name': 'Music',
                'verbose_name_plural': 'Musics',
                'ordering': ('created',),
            },
        ),
    ]
