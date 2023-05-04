# Generated by Django 4.2 on 2023-04-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('topic', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=800)),
                ('image', models.ImageField(upload_to='hero-images')),
            ],
            options={
                'verbose_name_plural': 'Hero_sections',
            },
        ),
    ]
