# Generated by Django 2.0.1 on 2018-05-07 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0005_user_main_merchant_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_main',
            old_name='merchant_id',
            new_name='Customer_id',
        ),
    ]
