# Generated by Django 2.0.1 on 2018-05-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0004_auto_20180501_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_main',
            name='merchant_id',
            field=models.CharField(default='hey', max_length=500),
        ),
    ]
