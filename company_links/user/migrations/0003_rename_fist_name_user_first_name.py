# Generated by Django 4.2.6 on 2024-07-04 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_level_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]