import re


def area_to_float(area_str):
    area = re.findall(r'\d{1,4}\.?\d{0,2}', area_str)
    return round(sum(map(float, area)), 2)


def price_to_float(price_str):
    prices = re.findall(r'\d+', price_str)
    if len(prices) == 1:
        return float(prices[0])
    else:
        return float(prices[0]) * 1000 + float(prices[1])


def get_currency(raw_price):
    if 'грн' in raw_price:
        return "UAH"
    elif '$' in raw_price:
        return "USD"
    elif '€' in raw_price:
        return 'EUR'