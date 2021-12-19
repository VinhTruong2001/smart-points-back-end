# Generated by Django 3.2.9 on 2021-12-19 02:54

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone
import user.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uid', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('displayName', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('profilePic', models.ImageField(null=True, upload_to=user.models.create_imgs_directory)),
                ('defaultGooglePhotoUrl', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('phone', models.CharField(default='', max_length=11, null=True)),
                ('gender', models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ')], default='M', max_length=1, null=True)),
                ('dateOfBirth', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('isPremium', models.BooleanField(default=False)),
                ('templateLiked', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None)),
                ('templateDownloaded', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uid', models.CharField(default=uuid.uuid4, editable=False, max_length=100, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
