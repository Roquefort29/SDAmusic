# Generated by Django 3.2 on 2022-12-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/'),
        ),
    ]