# Generated by Django 4.0 on 2024-03-18 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='is_actual',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='is_actual',
            new_name='is_active',
        ),
    ]