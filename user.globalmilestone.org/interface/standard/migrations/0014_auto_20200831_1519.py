# Generated by Django 3.1 on 2020-08-31 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0013_auto_20200831_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseinstance',
            name='primary_contact',
        ),
        migrations.RemoveField(
            model_name='courseinstance',
            name='tutors_teaching',
        ),
        migrations.RemoveField(
            model_name='session',
            name='tutor',
        ),
        migrations.AddField(
            model_name='course',
            name='primary_contact',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='courseinstance',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='standard.tutor'),
        ),
    ]