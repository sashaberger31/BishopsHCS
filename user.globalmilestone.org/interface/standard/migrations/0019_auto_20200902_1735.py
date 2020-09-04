# Generated by Django 3.1 on 2020-09-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0018_auto_20200902_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseinstance',
            name='students_enrolled',
        ),
        migrations.AddField(
            model_name='courseinstance',
            name='students_enrolled',
            field=models.ManyToManyField(to='standard.Student'),
        ),
    ]