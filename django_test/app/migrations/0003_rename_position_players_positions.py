# Generated by Django 4.2.6 on 2023-10-27 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_player_players'),
    ]

    operations = [
        migrations.RenameField(
            model_name='players',
            old_name='position',
            new_name='positions',
        ),
    ]
