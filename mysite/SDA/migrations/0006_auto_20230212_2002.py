# Generated by Django 3.2 on 2023-02-12 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SDA', '0005_auto_20230119_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albumArtist', to='SDA.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albumGenre', to='SDA.genre'),
        ),
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trackAlbum', to='SDA.album'),
        ),
        migrations.RemoveField(
            model_name='track',
            name='artist',
        ),
        migrations.AddField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='trackArtist', to='SDA.artist'),
        ),
        migrations.AlterField(
            model_name='track',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trackGenre', to='SDA.genre'),
        ),
    ]