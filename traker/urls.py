
from django.urls import path
from traker.views import index, delete_transaction,aichat,get_expense_ai_summary


urlpatterns = [
   
    path('',index),
    path('delete/<int:id>/', delete_transaction, name='delete_transaction'),
    path('aichat/', aichat ),
    path("api/expense-summary/", get_expense_ai_summary),

]