from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    main_balance = models.FloatField()
    emergency_balance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name']


class Transaction(models.Model):
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_acct = models.CharField(max_length=10, default='SAVINGS', choices=(
        ('SAVINGS', 'Savings'),
        ('EMERGENCY', 'Emergency'),
    )
                                        )
    transaction_type = models.CharField(max_length=10, default='DEPOSIT', choices=(
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAW', 'Withdraw'),
    )
                                        )
    transaction_amt = models.FloatField()
    transaction_user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-transaction_date']
