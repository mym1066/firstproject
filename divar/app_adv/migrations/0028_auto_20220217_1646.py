# Generated by Django 3.2.2 on 2022-02-17 13:16

import app_adv.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adv', '0027_alter_advertis_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertis',
            name='location',
        ),
        migrations.RemoveField(
            model_name='advertis',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='advertis',
            name='website',
        ),
        migrations.AddField(
            model_name='advertis',
            name='review',
            field=models.IntegerField(default=2, verbose_name='بازدید'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertis',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=app_adv.models.upload_image_path, verbose_name='تصویر'),
        ),
    ]
