# Generated by Django 3.1 on 2020-08-31 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0016_auto_20200831_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='parent_package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='standard.packagecourse'),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject_leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='standard.tutor'),
        ),
    ]
