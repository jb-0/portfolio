# Generated by Django 3.0.8 on 2020-07-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20200703_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
