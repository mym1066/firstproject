# Generated by Django 3.2.2 on 2022-02-14 20:35

import app_adv.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_adv', '0007_addadvertis_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to=app_adv.models.upload_gallery_image_path, verbose_name='تصویر')),
                ('advertis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_adv.advertis', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.AddField(
            model_name='addadvertis',
            name='website',
            field=models.CharField(default=2, max_length=20, verbose_name='وب سایت'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='addadvertis',
            table='addadvertis',
        ),
    ]
