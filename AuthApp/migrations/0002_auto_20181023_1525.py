# Generated by Django 2.0.6 on 2018-10-23 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='trasaction_user_id',
            new_name='transaction_user_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_acct',
        ),
    ]
