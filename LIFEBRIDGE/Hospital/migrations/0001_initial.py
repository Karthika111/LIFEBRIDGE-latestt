# Generated by Django 5.0.3 on 2024-04-17 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0009_alter_tbl_hospital_hospital_logo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_status', models.CharField(default=0, max_length=10)),
                ('complaint_title', models.CharField(max_length=100)),
                ('complaint_content', models.CharField(max_length=300)),
                ('complaint_reply', models.CharField(default='Not replied', max_length=100)),
                ('complaint_date', models.DateField(auto_now_add=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_hospital')),
            ],
        ),
    ]