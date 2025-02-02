# Generated by Django 4.2.7 on 2024-03-25 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0009_alter_tbl_hospital_hospital_logo_and_more'),
        ('User', '0016_tbl_deathcase'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_content', models.CharField(max_length=300)),
                ('feedback_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_status', models.CharField(default=0, max_length=10)),
                ('complaint_title', models.CharField(max_length=100)),
                ('complaint_content', models.CharField(max_length=300)),
                ('complaint_reply', models.CharField(default='Not replied', max_length=100)),
                ('complaint_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
