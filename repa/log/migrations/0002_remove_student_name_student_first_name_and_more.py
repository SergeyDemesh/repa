# Generated by Django 5.0.6 on 2024-05-09 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
