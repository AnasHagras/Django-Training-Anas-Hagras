# Generated by Django 4.1.2 on 2022-10-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_remove_album_status_remove_album_status_changed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=50)),
                ('song_image', models.ImageField(upload_to='songs/photos')),
                ('song_audio', models.FileField(upload_to='songs/files')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
