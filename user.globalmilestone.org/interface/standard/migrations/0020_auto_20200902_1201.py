# Generated by Django 3.1 on 2020-09-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0019_auto_20200902_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='students_attended',
            field=models.ManyToManyField(blank=True, related_name='sessions_attended', to='standard.Student'),
        ),
        migrations.AlterField(
            model_name='session',
            name='students_attending',
            field=models.ManyToManyField(blank=True, related_name='sessions_attending', to='standard.Student'),
        ),
    ]
