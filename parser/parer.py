from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import requests

from utils import *


class ParseSession:

    def __init__(self):
        self.session = requests.Session()
        self.headers = get_headers()

    def __call__(self, page=1, filter='аренда-квартир-киев'):
        cyrillic_part_url = urllib.request.quote(filter)
        response = self.session.get('https://www.lun.ua/{}?page={}'.format(cyrillic_part_url, page),
                                    headers=self.headers)
        return response.text

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.session.close()


def get_headers():
    """
    Указываем настройки барузера в заголовках http запроса
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}

    return headers


def get_name(bsObj, flag="standard"):
    if flag == "standard":
        title = bsObj.find("div", {"class": "realty-card-header-title"})
    else:
        title = bsObj.find('div', {"class": "jss93"})

    return title.get_text()


def get_price(bsObj, flag="standard"):
    if flag == "standard":
        price = bsObj.find("div", {"class": "realty-card-characteristics__price"})
    else:
        price = bsObj.find("div", {"class": "jss109"})

    return price.get_text()


def get_area(bsObj, flag="standard"):
    if flag == "standard":
        area = bsObj.findAll("div", {"class": "realty-card-characteristics-list__item"})
    else:
        area = bsObj.findAll("li")

    # Ждем исключения, если не указана площадь.
    try:
        return area[1].get_text()
    except IndexError as ae:
        return "Информация не найдена"


def get_district(bsObj, flag="standard"):
    if flag == "standard":
        district = bsObj.find("p", {"class": "realty-card-header__subtitle"}).find("a")
    else:
        district = bsObj.find("div", {"class": "jss98"}).find("a")

    try:
        return district.get_text()
    except AttributeError as ae:
        return "Информация не найдена"


def get_url(bsObj, flag="standard"):
    if flag == "standard":
        mediator_url = bsObj.find("a", {"class": "realty-card-header__link-wrapper"})["href"]
    else:
        mediator_url = bsObj.find("a", {"class": "jss92"})["href"]
    new_bsObj = BeautifulSoup(urlopen("https://www.lun.ua{}".format(mediator_url)), "html.parser")

    main_url = new_bsObj.find("title").get_text()

    return main_url


def get_data_from_page(bsObj, data):
    """
    Получаем данные с конкретной страницы
    """
    # Проверяем загрузилась ли страница полностью или есть js код
    if bsObj.find("div", {"class": "cards-container"}):
        flag = "standard"
        houses_info = bsObj.findAll("div", {"class": "realty-card-inner"})
    else:
        flag = "jss"
        houses_info = bsObj.findAll("div", {"class": "jss89"})

    for house_info in houses_info:
        try:
            price = get_price(house_info, flag)
            area = get_area(house_info, flag)
            house_data = {"name": get_name(house_info, flag), "price": clean_price(price),
                        "area": clean_area(area), "district": get_district(house_info, flag),
                        "url": get_url(house_info, flag), 'currency': clean_currency(price)}
        except:
            print('One flat is skipped')
            continue
        data.append(house_data)

    return data


def check_next_page_exist(bsObj):
    """
    Проверяем есть ли следующая страница
    """
    if bsObj.find("link", {"rel": "next"}):
        return True

    return False


def get_data():
    with ParseSession() as get_html:
        data = []
        print("Сканирем страницу № 1")
        bsObj = BeautifulSoup(get_html(), "html.parser")
        get_data_from_page(bsObj, data)

        page_number = 1
        while check_next_page_exist(bsObj):
            page_number += 1

            if page_number == 3:
                return data

            print("Существует страница №", page_number)
            print("Сканирем страницу №", page_number)
            bsObj = BeautifulSoup(get_html(page_number), "html.parser")
            get_data_from_page(bsObj, data)

    return data


def parse_data():
    data = get_data()
    return data

# if __name__ == '__main__':
#    main()

