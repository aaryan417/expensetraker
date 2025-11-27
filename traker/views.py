from django.shortcuts import render,redirect
from .models import currentbalence, transaction
# Create your views here.



def index(request):
    if request.method =="POST":
        discription=request.POST.get("discription")
        amount=request.POST.get("amount")
        
        expense_type="debit"
        if float(amount)<0:
            expense_type="credit"
        balence, _ =currentbalence.objects.get_or_create(id=1)
        transaction_history=transaction.objects.create(amount=amount,
                                                    expense_type=expense_type,
                                                    balence=balence,
                                                    discription=discription)
        balence.blance+=float(transaction_history.amount)
        balence.save()

        print (discription,amount)
        return redirect('/')
    return render (request, "index.html")    
