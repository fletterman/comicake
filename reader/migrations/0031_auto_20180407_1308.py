# Generated by Django 2.0.2 on 2018-04-07 20:08

from django.db import migrations, models
import reader.models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0030_auto_20180326_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='file',
            field=models.ImageField(height_field=models.PositiveSmallIntegerField(editable=False, null=True), upload_to=reader.models.Page.path, width_field=models.PositiveSmallIntegerField(editable=False, null=True)),
        ),
    ]
