# Generated by Django 4.2.7 on 2024-03-21 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_tbl_donatingorgan'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_nominee',
            name='donor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.tbl_donateform'),
        ),
    ]
