# Generated by Django 4.2 on 2023-05-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_images')),
                ('name', models.CharField(max_length=300)),
                ('topic', models.CharField(max_length=200)),
                ('description_1', models.TextField(max_length=600)),
                ('description_2', models.TextField(max_length=600)),
                ('about1', models.CharField(max_length=200)),
                ('about2', models.CharField(max_length=200)),
                ('about3', models.CharField(max_length=200)),
                ('about4', models.CharField(max_length=200)),
                ('about5', models.CharField(max_length=200)),
                ('about6', models.CharField(max_length=200)),
            ],
        ),
    ]
