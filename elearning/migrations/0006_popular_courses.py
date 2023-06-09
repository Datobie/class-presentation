# Generated by Django 4.2 on 2023-05-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0005_remove_course_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular_courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Popular_images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('duration', models.TextField(max_length=100)),
                ('students', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Popular_courses',
            },
        ),
    ]
