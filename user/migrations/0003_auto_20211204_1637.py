# Generated by Django 3.2.9 on 2021-12-04 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_userinfo_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='dateOfBirth',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ')], default='M', max_length=1, null=True),
        ),
    ]