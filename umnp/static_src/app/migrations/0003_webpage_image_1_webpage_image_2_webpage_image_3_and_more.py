# Generated by Django 4.1.3 on 2022-12-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_webpage_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='webpage',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='webpage',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='webpage',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
