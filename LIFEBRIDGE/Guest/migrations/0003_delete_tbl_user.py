# Generated by Django 5.0.1 on 2024-02-13 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_tbl_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_user',
        ),
    ]