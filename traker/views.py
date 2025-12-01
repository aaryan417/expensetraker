from django.shortcuts import render,redirect,get_object_or_404
from .models import Currentbalence, Transaction
from django.http import JsonResponse
# Create your views here.

def aichat(request):
     return render(request, "aichat.html")

def index(request):
    if request.method =="POST":
        discription=request.POST.get("discription")
        amount=request.POST.get("amount")
        if not amount:
             amount = 0
        else:
             amount = float(amount)
        
        if amount >= 0:
             expense_type = "credit"
        else:
             expense_type = "debit"
             amount = abs(amount)
        
        balence, _ =Currentbalence.objects.get_or_create(id=1)
        transaction_history=Transaction.objects.create(amount=amount,
                                                    expense_type=expense_type,
                                                    balence=balence,
                                                    discription=discription)
        

        if expense_type == "credit":
             balence.balence += amount

              
        else:
             balence.balence -= amount
             

        balence.save()

        #
        return redirect('/')
    balence, _ =Currentbalence.objects.get_or_create(id=1)
    

    expenses=0
    income=0
    for t in Transaction.objects.all():
        if t.expense_type == "credit":
             income+=t.amount
        else:
             expenses+=t.amount

    context={'transactions':Transaction.objects.all(),
             'balence' : balence,
             'expenses':expenses,
             'income':income,
             
             }
    print (balence)
    return render (request, "index.html",context) 

def get_expense_ai_summary(request):
    balance = Currentbalence.objects.first()

    transactions = Transaction.objects.all().order_by('-created_at')

    total_credit = sum(t.amount for t in transactions if t.expense_type == "credit")
    total_debit = sum(t.amount for t in transactions if t.expense_type == "debit")

    # Category-wise breakdown
    category_summary = {}
    for t in transactions:
        cat = t.expense_type
        category_summary[cat] = category_summary.get(cat, 0) + t.amount

    # Last 10 transactions only
    recent_transactions = list(transactions.values()[:10])

    return JsonResponse({
        "balance": balance.balence if balance else 0,
        "total_credit": total_credit,
        "total_debit": total_debit,
        "category_summary": category_summary,
        "recent_transactions": recent_transactions,
        "total_transactions": transactions.count()
    })






def delete_transaction(request, id):
    trans= get_object_or_404(Transaction, id=id)
    balence = trans.balence
    if trans.expense_type == "credit":
        balence.balence -= trans.amount
    else:
        balence.balence += trans.amount
    balence.save()
    trans.delete()
    return redirect('/')