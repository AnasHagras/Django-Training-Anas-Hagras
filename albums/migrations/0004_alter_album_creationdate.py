# Generated by Django 4.1.1 on 2022-10-19 20:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_alter_album_creationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creationDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
