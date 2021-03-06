# Generated by Django 2.0.6 on 2018-10-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApp', '0002_auto_20181023_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_acct',
            field=models.CharField(choices=[('SAVINGS', 'Savings'), ('EMERGENCY', 'Emergency')], default='SAVINGS', max_length=10),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAW', 'Withdraw')], default='DEPOSIT', max_length=10),
        ),
    ]
