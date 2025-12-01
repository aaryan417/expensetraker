from django.contrib import admin
from traker.models import*

# Register your models here.
admin.site.site_header="Expense Traker"
# admin.site.site_url="Expense Traker"
admin.site.site_title="Expense Traker"

admin.site.register(Currentbalence)
class Transaction_admin(admin.ModelAdmin):
    list_display =[
        
        "balence",
        "amount",
        "expense_type",
        "discription",
        "created_at",
        "amount_type"
    ]
    def amount_type(self, obj):
        if obj.amount>0:
            return "positive"
        return "negative"
    
    search_fields=['expense_type',"discription"]
    list_filter=['expense_type']
admin.site.register(Transaction,Transaction_admin)
