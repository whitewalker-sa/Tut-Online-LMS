# Generated by Django 2.2.13 on 2020-12-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0020_auto_20201219_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='temporary_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
