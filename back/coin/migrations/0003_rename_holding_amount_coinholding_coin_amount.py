# Generated by Django 3.2.3 on 2021-05-21 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0002_auto_20210521_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coinholding',
            old_name='holding_amount',
            new_name='coin_amount',
        ),
    ]