# Generated by Django 3.1.2 on 2020-10-22 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descriptions',
            new_name='description',
        ),
    ]