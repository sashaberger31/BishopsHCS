# Generated by Django 3.1 on 2020-08-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('contact_email', models.EmailField(default='', max_length=254)),
                ('age', models.IntegerField(default=1)),
                ('us_grade', models.IntegerField(default=1)),
                ('slack_email', models.EmailField(default='', max_length=254)),
                ('gclass_email', models.EmailField(default='', max_length=254)),
                ('teaching_hours', models.TextField(default='')),
                ('prep_hours', models.TextField(default='')),
                ('cs_hours_sem', models.IntegerField(default=0)),
                ('course_assignment_code', models.CharField(default='', max_length=1000)),
                ('tutoring_history', models.TextField(default='')),
                ('attendance_record', models.TextField(default='')),
                ('admin_extra', models.TextField(default='')),
                ('random_id', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WebText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
            ],
        ),
    ]
