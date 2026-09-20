from rest_framework import serializers

class CommonParams(serializers.Serializer):
    quantity = serializers.IntegerField(required=False, default=10, min_value=1)

class AccountNumbersParams(CommonParams):
    digits = serializers.IntegerField(default=8)
    mask_digits = serializers.BooleanField(default=False)
    
class TransactionsParams(CommonParams):
    currency = serializers.CharField(default="USD")

class CurrenciesParams(CommonParams):
    code = serializers.ListField(child=serializers.CharField(), required=False, default=list, source="codes")
    random_currencies = serializers.BooleanField(default=False)

class StocksParams(CommonParams):
    symbol = serializers.CharField(default=None)