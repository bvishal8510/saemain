# Generated by Django 2.0.1 on 2018-04-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0002_auto_20180419_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_main',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user_main',
            name='meter_no',
            field=models.IntegerField(),
        ),
    ]
