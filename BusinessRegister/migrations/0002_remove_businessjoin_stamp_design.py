# Generated by Django 3.1.5 on 2021-01-11 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessRegister', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessjoin',
            name='stamp_design',
        ),
    ]