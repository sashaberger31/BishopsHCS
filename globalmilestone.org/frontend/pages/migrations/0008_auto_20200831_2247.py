# Generated by Django 3.1 on 2020-08-31 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20200831_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='link',
            field=models.URLField(default='', max_length=100),
        ),
    ]
