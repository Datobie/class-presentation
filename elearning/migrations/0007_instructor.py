# Generated by Django 4.2 on 2023-05-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0006_popular_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='instructor_images')),
                ('name', models.CharField(max_length=300)),
                ('designation', models.CharField(max_length=200)),
            ],
        ),
    ]
