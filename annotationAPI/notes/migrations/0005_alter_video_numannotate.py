# Generated by Django 4.1.4 on 2023-04-10 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0004_audio_numannotate_video_numannotate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="numAnnotate",
            field=models.IntegerField(default=0),
        ),
    ]