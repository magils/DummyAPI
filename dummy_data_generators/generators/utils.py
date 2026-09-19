from datetime import datetime, timedelta
import random

def random_date(days_back=30):
    rand_days_back = random.randint(0, 30)
    return datetime.now() - timedelta(days=rand_days_back)

def random_date_with_format(format, days_back=30):
    rand_date = random_date(days_back)
    return rand_date.strftime(format)

def random_numeric_value(number, start_at=0):
    return round(random.uniform(start_at, number), 2)
