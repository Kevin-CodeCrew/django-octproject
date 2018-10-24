from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from AuthApp.models import Customer, Transaction


def index(request):
    customer = get_object_or_404(Customer, pk=1)
    transactions = Transaction.objects.filter(transaction_user_id__pk=1)
    return render(request, 'AuthApp/transhistory.html', {'customer': customer, 'transactions': transactions})


def transaction(request):
    customer = get_object_or_404(Customer, pk=1)
    if request.method == "POST":
        deposit_amt = float(request.POST['trans_value'])
        deposit_type = request.POST['trans_type']
        deposit_acct = request.POST['trans_acct']

        # UPDATE THE RUNNING BALANCE
        if deposit_type != 'DEPOSIT':
            deposit_amt: float = deposit_amt * -1
        if deposit_acct == 'SAVINGS':
            customer.main_balance += deposit_amt
        else:
            customer.emergency_balance += deposit_amt
        print(deposit_amt, deposit_type, deposit_acct)
        customer.save()
        # NOW UPDATE TRANSACTION HISTORY
        thist = Transaction(id=None, transaction_acct=deposit_acct, transaction_type=deposit_type,
                            transaction_amt=deposit_amt,
                            transaction_user_id=customer)
        thist.save()
        return redirect('index')
    else:
        return render(request, 'AuthApp/transaction.html', {'customer': customer})
