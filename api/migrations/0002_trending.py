# Generated by Django 4.1.3 on 2022-11-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
                ('place_image', models.ImageField(upload_to='trending_images')),
                ('place_location', models.CharField(max_length=100)),
                ('trending_item', models.CharField(max_length=100)),
            ],
        ),
    ]