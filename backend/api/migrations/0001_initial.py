# Generated by Django 3.1 on 2021-11-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100, verbose_name='Name')),
                ('email', models.EmailField(default='', max_length=100, verbose_name='email')),
                ('password', models.CharField(default='', max_length=100, verbose_name='password')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
