# Generated by Django 3.1 on 2020-08-31 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20200831_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='link',
            field=models.CharField(default='', max_length=100),
        ),
    ]
