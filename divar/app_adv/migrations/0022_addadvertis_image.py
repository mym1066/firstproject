# Generated by Django 3.2.2 on 2022-02-15 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adv', '0021_remove_addadvertis_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='addadvertis',
            name='image',
            field=models.ImageField(blank=True, max_length=20, null=True, upload_to='', verbose_name='عکس'),
        ),
    ]
