# Generated by Django 3.2.2 on 2022-02-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adv', '0014_alter_addadvertis_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addadvertis',
            name='image',
            field=models.ImageField(blank=True, max_length=20, null=True, upload_to='', verbose_name='عکس'),
        ),
    ]
