# Generated by Django 3.0.6 on 2020-05-24 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0002_auto_20200523_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.CharField(default=django.utils.timezone.now, max_length=2000),
            preserve_default=False,
        ),
    ]
