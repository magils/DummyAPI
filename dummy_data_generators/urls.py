from django.urls import path
from dummy_data_generators.views import finance

urlpatterns = [
    path("finance/account-numbers", finance.account_numbers_list, name ="account_numbers"),
    path("finance/transactions", finance.transactions_list),
    path("finance/currencies", finance.currency_list)
]