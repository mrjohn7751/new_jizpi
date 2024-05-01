# Generated by Django 3.2.25 on 2024-04-25 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryElon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Kategoriya nomi')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryFacultet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Kategoriya nomi')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Kategoriya nomi')),
            ],
        ),
        migrations.CreateModel(
            name='ekranImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Photos/ekran_IMG/')),
            ],
            options={
                'verbose_name': 'Ekran Rasmi',
                'verbose_name_plural': 'Ekran Rasmlari',
            },
        ),
        migrations.CreateModel(
            name='ArticleNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Sarlovha')),
                ('body', models.TextField(verbose_name='Tana qismi')),
                ('img', models.ImageField(upload_to='Photos/Yangiliklar/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.categorynews')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleFacultet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Sarlovha')),
                ('body', models.TextField(verbose_name='Tana qismi')),
                ('img', models.ImageField(upload_to='Photos/Yangiliklar/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.categorynews')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleElon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Sarlovha')),
                ('body', models.TextField(verbose_name='Tana qismi')),
                ('img', models.ImageField(upload_to='Photos/Yangiliklar/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.categorynews')),
            ],
        ),
    ]
