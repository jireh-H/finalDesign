# Generated by Django 3.0.6 on 2020-05-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
