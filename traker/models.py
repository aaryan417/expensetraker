from django.db import models

# Create your models here.
class Currentbalence(models.Model):
    balence=models.FloatField(default=0)


class Transaction(models.Model):
    balence=models.ForeignKey(Currentbalence, on_delete=models.CASCADE)
    amount=models.FloatField()
    expense_type=models.CharField(max_length=10, choices=[
            ('credit', 'credit'),
            ('debit', 'debit')
        ])
    discription=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now=True)
    # created_at=models.DateTimeField(auto_now_add=True)
    


    def __str__(self) ->str:
        return f"the amount is {self.amount} for {self.discription}" 