# Generated by Django 3.2.2 on 2022-01-24 18:56

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_category', '0003_rename_advertiscategory_appcategory'),
        ('app_adv', '0006_rename_categorys_advertis_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Addadvertis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('phone_number', models.CharField(max_length=12, verbose_name='شماره تماس')),
                ('description', models.TextField(verbose_name=' توضیحات تکمیلی')),
                ('categories', models.ManyToManyField(blank=True, to='app_category.AppCategory', verbose_name='دسته بندی ها')),
            ],
        ),
    ]
