# Generated by Django 3.1.12 on 2025-03-06 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lootify_test', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song_file',
            new_name='audio',
        ),
    ]
