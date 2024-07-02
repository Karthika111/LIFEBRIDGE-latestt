# Generated by Django 4.2.7 on 2024-03-25 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0009_alter_tbl_hospital_hospital_logo_and_more'),
        ('User', '0012_tbl_donateform_donateform_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_status', models.CharField(default=0, max_length=10)),
                ('requested_date', models.DateField(auto_now_add=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_donateform')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]