# Generated by Django 2.0.2 on 2018-04-07 20:45

from django.db import migrations, models
import reader.models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0032_auto_20180407_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='file',
            field=models.ImageField(height_field='height', max_length=200, upload_to=reader.models.Page.path, width_field='width'),
        ),
    ]
