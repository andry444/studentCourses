# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 12:33
from __future__ import unicode_literals

import courses.models
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_enumfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_title', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'courses',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'User',
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CourseOffering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=100, verbose_name='course_title')),
                ('prerequisites', models.TextField(blank=True, max_length=500, verbose_name='prerequisites')),
            ],
        ),
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_mark', models.IntegerField(null=True, verbose_name='first mark')),
                ('second_mark', models.IntegerField(null=True, verbose_name='second mark')),
                ('third_mark', models.IntegerField(null=True, verbose_name='third mark')),
                ('forth_mark', models.IntegerField(null=True, verbose_name='forth mark')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('post', django_enumfield.db.fields.EnumField(default=2, enum=courses.models.PostChoices, verbose_name='post')),
                ('department', django_enumfield.db.fields.EnumField(default=0, enum=courses.models.DepartmentChoices, verbose_name='department')),
            ],
            options={
                'verbose_name': 'Professor',
            },
            bases=('courses.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('year_in_university', django_enumfield.db.fields.EnumField(default=1, enum=courses.models.YearChoices, verbose_name='year')),
                ('group', models.IntegerField(verbose_name='group')),
                ('department', django_enumfield.db.fields.EnumField(default=0, enum=courses.models.DepartmentChoices, verbose_name='department')),
                ('courses', models.ManyToManyField(to='courses.CourseOffering')),
            ],
            options={
                'verbose_name': 'Student',
            },
            bases=('courses.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='reportcard',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Student'),
        ),
        migrations.AddField(
            model_name='courseoffering',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Professor'),
        ),
    ]
