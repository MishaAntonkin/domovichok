import re


def chunk_generator(data, piece):
    if not data:
        raise Exception('no data to slice')
    elif piece < 1:
        raise Exception('no sence to slice')
    for i, inx in enumerate(data[::piece]):
        yield data[i*piece:(i+1)*piece]


def clean_area(area_str):
    area = re.findall(r'\d{1,4}\.?\d{0,2}', area_str)[0]
    return round(float(area), 2)


def clean_price(price_str):
    prices = re.findall(r'\d+', price_str)
    if len(prices) == 1:
        return float(prices[0])
    else:
        return float(prices[0]) * 1000 + float(prices[1])


def clean_currency(raw_price):
    if 'грн' in raw_price:
        return "UAH"
    elif '$' in raw_price:
        return "USD"
    elif '€' in raw_price:
        return 'EUR'
