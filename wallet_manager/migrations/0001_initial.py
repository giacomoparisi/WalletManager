# Generated by Django 4.0 on 2021-12-16 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('HOME', 'Home'), ('FOOD', 'Food'), ('SERVICES', 'Services'), ('CLOTHING', 'Clothing'), ('HEALTH', 'Health'), ('TRANSPORT', 'Transport'), ('ENTERTAINMENT', 'Entertainment'), ('MISCELLANEOUS', 'Miscellaneous')], default='MISCELLANEOUS', max_length=20)),
                ('descritpion', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
