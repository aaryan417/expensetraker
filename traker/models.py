from django.db import models

# Create your models here.
class currentbalence(models.Model):
    blance=models.FloatField(default=0)


class transaction(models.Model):
    balence=models.ForeignKey(currentbalence, on_delete=models.CASCADE)
    amount=models.FloatField()
    expense_type=models.CharField(max_length=10, choices=[
            ('credit', 'credit'),
            ('debit', 'debit')
        ])
    discription=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now=True)
    # created_at=models.DateTimeField(auto_now_add=True)
    