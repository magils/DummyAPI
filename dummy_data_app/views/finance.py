from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dummy_data_app.generators.finance import generate_account_numbers, generate_transactions, generate_currency_list, generate_stocks
from dummy_data_app.views.http_methods import HttpMethod
from dummy_data_app.serializers import AccountNumbersParams, TransactionsParams, CurrenciesParams, StocksParams
from dummy_data_app.views.decorators import view_query_params


@api_view([HttpMethod.GET])
@view_query_params(AccountNumbersParams)
def account_numbers(request, params):
    account_numbers = generate_account_numbers(params.quantity, params.digits, params.mask_digits)
    return Response({"account_numbers": account_numbers})

@api_view([HttpMethod.GET])
@view_query_params(TransactionsParams)
def transactions(request, params):
    transactions = generate_transactions(params.quantity, params.currency)
    return Response({"transactions": transactions})

@api_view([HttpMethod.GET])
@view_query_params(CurrenciesParams)
def currencies(request, params):
    currencies = generate_currency_list(params.quantity, params.codes, params.random_currencies)
    return Response({"currencies": currencies})    

@api_view([HttpMethod.GET])
@view_query_params(StocksParams)
def stocks(request, params):
    stocks = generate_stocks(params.quantity, params.symbol)
    resp_status = status.HTTP_200_OK if stocks else status.HTTP_404_NOT_FOUND

    return Response({"stocks": stocks}, status = resp_status)   
