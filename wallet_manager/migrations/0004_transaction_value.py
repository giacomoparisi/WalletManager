# Generated by Django 4.0 on 2021-12-18 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_manager', '0003_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
