# Generated by Django 4.2.4 on 2023-08-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('slug', models.CharField(max_length=200, verbose_name='Slug')),
                ('body', models.TextField(verbose_name='Текст статьи')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Фото')),
                ('creation_date', models.DateTimeField(verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('view_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
