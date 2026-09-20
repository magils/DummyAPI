from datetime import timedelta, datetime
import random
import string
import secrets

from dummy_data_app.generators.utils import (
    random_date,
    random_numeric_value
)
from dummy_data_app.generators.finance_constants import (
    TRANSACTION_CATEGORIES,
    TRANSACTION_MERCHANTS,
    TRANSACTION_TYPES,
    CURRENCIES,
    STOCKS
)

TRANSACTION_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Helper functions
def _random_digits(digits):
    return "".join(random.choice(string.digits) for _ in range(digits))


# Finance Methods generators

def generate_account_number(length=8, mask_digits=False):
    routing_digit = random.choice(string.digits[1:])
    fake_routing_prefix = f"0{routing_digit}1"

    if mask_digits:
        account_digits = _random_digits(4)
        masked_portion = "*" * (length - 4)
        return fake_routing_prefix + masked_portion + account_digits

    account_digits = _random_digits(length)
    account_number = fake_routing_prefix + account_digits

    return account_number


def generate_account_numbers(quantity, length=8, mask_digits=False):
    account_numbers = [
        generate_account_number(length, mask_digits) for _ in range(quantity)
    ]
    return account_numbers


def generate_transactions(quantity=5, currency="USD"):
    transactions = []

    for _ in range(quantity):
        txn_date = random_date()
        type = random.choice(TRANSACTION_TYPES)
        posted_date = txn_date + timedelta(days=random.randint(1,3))
        raw_amount = random_numeric_value(9999.99)
        amount = -1 * raw_amount if type == "debit" else raw_amount
        merchant = random.choice(TRANSACTION_MERCHANTS)
        category = random.choice(TRANSACTION_CATEGORIES)

        tx = {
            "transaction_id": secrets.token_hex(16),
            "account_number": generate_account_number(),
            "date": txn_date.strftime(TRANSACTION_DATE_FORMAT),
            "posted_date": posted_date.strftime(TRANSACTION_DATE_FORMAT),
            "description": f"Transaction approved - Concept: {category} {merchant}",
            "merchant": merchant,
            "category": category,
            "type": type,
            "amount": amount,
            "balance":  random_numeric_value(1999.99),
            "status": "posted",
            "currency": currency,
        }

        transactions.append(tx)

    return transactions

def generate_currency_list(quantity=None, codes=[], random_currencies=False):

    if quantity:
        currencies = CURRENCIES

        if random_currencies:
            currencies = random.sample(currencies, len(currencies))

        return currencies[:quantity]
    elif codes:
        codes = list(map(lambda c: c.lower(), codes))
        filtered_currencies = filter(lambda c: c["code"].lower() in codes, CURRENCIES)
        return list(filtered_currencies)
    else:
        return CURRENCIES



def generate_stocks(quantity=10, symbol=None):
    stocks = []

    if symbol:
        stock_entries = [(symbol, STOCKS.get(symbol))] if symbol in STOCKS else []
    else:
        stock_entries = list(STOCKS.items())[:quantity]

    for symbol, stock_data  in stock_entries:
        stock =  {
            "symbol": symbol,
            "exchange": "NASDAQ",
            "currency": "USD",
            "sector": stock_data["sector"],
            "industry": stock_data["industry"],
            "price": random_numeric_value(1500, start_at=1),
            "previousClose": random_numeric_value(1500, start_at=1),
            "open": random_numeric_value(1500, start_at=1),
            "dayHigh": random_numeric_value(1500, start_at=1),
            "dayLow": random_numeric_value(1500, start_at=1),
            "change": random_numeric_value(1500, start_at=1),
            "changePercent": random_numeric_value(1500, start_at=1),
            "volume": random_numeric_value(12345678, start_at=1000, only_integer=True),
            "sharesOutstanding": random_numeric_value(1234567890, start_at=1, only_integer=True),
            "marketCap": random_numeric_value(1234567890, start_at=1, only_integer=True),
            "eps": random_numeric_value(1234, start_at=1),
            "peRatio": random_numeric_value(200, start_at=1),
            "dividendYield": random_numeric_value(1, start_at=0.1),
            "week52High": random_numeric_value(1500, start_at=1),
            "week52Low": random_numeric_value(1500, start_at=1),
            "beta": random_numeric_value(10, start_at=0.1),
            "lastUpdated": datetime.now().strftime(TRANSACTION_DATE_FORMAT)
        }

        stocks.append(stock)

    return stocks

