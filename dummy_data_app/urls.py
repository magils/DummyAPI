from django.urls import path
from dummy_data_app.views import finance

urlpatterns = [
    path("finance/account-numbers", finance.account_numbers),
    path("finance/transactions", finance.transactions),
    path("finance/currencies", finance.currencies),
    path("finance/stocks", finance.stocks)
]