# Generated by Django 4.0.3 on 2022-03-04 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_remove_form_id_form_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='TCNumber',
        ),
        migrations.RemoveField(
            model_name='form',
            name='tel',
        ),
    ]
