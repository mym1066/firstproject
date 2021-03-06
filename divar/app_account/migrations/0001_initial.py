# Generated by Django 3.2.2 on 2021-12-31 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bakhsh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('amar_code', models.IntegerField(verbose_name='Amar Code')),
            ],
            options={
                'verbose_name': 'Bakhsh',
                'verbose_name_plural': 'Bakhshs',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Ostan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('amar_code', models.IntegerField(verbose_name='Amar Code')),
            ],
            options={
                'verbose_name': 'Ostan',
                'verbose_name_plural': 'Ostans',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Shahrestan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('amar_code', models.IntegerField(verbose_name='Amar Code')),
                ('ostan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shahrestans', to='app_account.ostan', verbose_name='Ostan')),
            ],
            options={
                'verbose_name': 'Shahrestan',
                'verbose_name_plural': 'Shahrestans',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Shahr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('amar_code', models.IntegerField(verbose_name='Amar Code')),
                ('shahr_type', models.IntegerField(verbose_name='Shahr Type')),
                ('bakhsh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shahrs', to='app_account.bakhsh', verbose_name='Bakhsh')),
                ('ostan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shahrs', to='app_account.ostan', verbose_name='Ostan')),
                ('shahrestan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shahrs', to='app_account.shahrestan', verbose_name='Shahrestan')),
            ],
            options={
                'verbose_name': 'Shahr',
                'verbose_name_plural': 'Shahrs',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Dehestan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('amar_code', models.IntegerField(verbose_name='Amar Code')),
                ('bakhsh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dehestans', to='app_account.bakhsh', verbose_name='Bakhsh')),
                ('ostan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dehestans', to='app_account.ostan', verbose_name='Ostan')),
                ('shahrestan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dehestans', to='app_account.shahrestan', verbose_name='Shahrestan')),
            ],
            options={
                'verbose_name': 'Dehestan',
                'verbose_name_plural': 'Dehestans',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='bakhsh',
            name='ostan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bakhshs', to='app_account.ostan', verbose_name='Ostan'),
        ),
        migrations.AddField(
            model_name='bakhsh',
            name='shahrestan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bakhshs', to='app_account.shahrestan', verbose_name='Shahrestan'),
        ),
        migrations.CreateModel(
            name='Abadi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('amar_code', models.IntegerField(verbose_name='Amar Code')),
                ('abadi_type', models.IntegerField(verbose_name='Abadi Type')),
                ('bakhsh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abadies', to='app_account.bakhsh', verbose_name='Bakhsh')),
                ('dehestan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abadies', to='app_account.dehestan', verbose_name='Dehestan')),
                ('ostan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abadies', to='app_account.ostan', verbose_name='Ostan')),
                ('shahrestan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abadies', to='app_account.shahrestan', verbose_name='Shahrestan')),
            ],
            options={
                'verbose_name': 'Abadi',
                'verbose_name_plural': 'Abadies',
                'ordering': ('id',),
            },
        ),
    ]
