from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dummy_data_app.generators.finance import generate_account_numbers, generate_transactions, generate_currency_list
from dummy_data_app.views.http_methods import HttpMethod


@api_view([HttpMethod.GET])
def account_numbers_list(request):
    try:
        digits = int(request.query_params.get("digits", 8))
        mask_digits = request.query_params.get("mask_digits", "false").lower() == "true"
        quantity = int(request.query_params.get("quantity", 5))
    except TypeError as te:
        return Response({"error": f"Invalid query param(s)."}, status=status.HTTP_400_BAD_REQUEST)

    account_numbers = generate_account_numbers(quantity, digits, mask_digits)

    return Response({"account_numbers": account_numbers})


@api_view([HttpMethod.GET])
def transactions_list(request):
    try:
        quantity = int(request.query_params.get("quantity", 10))
        currency = request.query_params.get("currency") or "USD"
    except TypeError:
        return Response({"error": f"Invalid query param(s)."}, status=status.HTTP_400_BAD_REQUEST)

    transactions = generate_transactions(quantity, currency)
    return Response({"transactions": transactions})


@api_view([HttpMethod.GET])
def currency_list(request):
    try:
        quantity = int(request.query_params.get("quantity")) if "quantity" in request.query_params else None
        codes = request.query_params.getlist("code") or []
        random_currencies = request.query_params.get("random_currencies", "").lower() == "true"
    except TypeError:
        return Response({"error": f"Invalid query param(s)."}, status=status.HTTP_400_BAD_REQUEST)

    currencies = generate_currency_list(quantity,codes, random_currencies)
    return Response({"currencies": currencies})    

    
