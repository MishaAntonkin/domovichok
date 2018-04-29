from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib


def get_html(page=1, filter='аренда-квартир-киев'):
    """
    Получаем html сайта
    """
    cyrillic_part_url = urllib.request.quote(filter)
    response = urlopen('https://www.lun.ua/{}?page={}'.format(cyrillic_part_url, page))
    return response


def get_name(bsObj):
    title = bsObj.findAll("div", {"class": "realty-card-header-title"})

    return title[0].get_text()


def get_name_jss(bsObj):
    title = bsObj.find('div', {"class": "jss93"})

    return title.get_text()


def get_price(bsObj):
    price = bsObj.findAll("div", {"class": "realty-card-characteristics__price"})

    return price[0].get_text()


def get_price_jss(bsObj):
    price = bsObj.find("div", {"class": "jss109"})

    return price.get_text()


def get_area(bsObj):
    area = bsObj.findAll("div", {"class": "realty-card-characteristics-list__item"})

    # Ждем исключения, если не указана площадь.
    try:
        return area[1].get_text()
    except IndexError as ae:
        return "Информация не найдена"


def get_area_jss(bsObj):
    area = bsObj.findAll("li")

    try:
        return area[1].get_text()
    except IndexError as ae:
        return "Информация не найдена"


def get_district(bsObj):
    district = bsObj.find("p", {"class": "realty-card-header__subtitle"}).find("a")

    try:
        return district.get_text()
    except AttributeError as ae:
        return "Информация не найдена"


def get_district_jss(bsObj):
    district = bsObj.find("div", {"class": "jss98"}).find("a")

    try:
        return district.get_text()
    except AttributeError as ae:
        return "Информация не найдена"


def get_data_from_page(bsObj, data):
    """
    Получаем данные с конкретной страницы
    """
    # Проверяем загрузилась ли страница полностью или есть js код
    if bsObj.find("div", {"class": "cards-container"}):
        # Если html не содержит js
        for house_info in bsObj.findAll("div", {"class": "realty-card-inner"}):
            house_data = {"name": get_name(house_info), "price": get_price(house_info),
                          "area": get_area(house_info), "district": get_district(house_info)}

            data.append(house_data)
    else:
        # Если html содержит js
        for house_info in bsObj.findAll("div", {"class": "jss89"}):
            house_data = {"name": get_name_jss(house_info), "price": get_price_jss(house_info),
                          "area": get_area_jss(house_info), "district": get_district_jss(house_info)}

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

print(parse_data())
#if __name__ == '__main__':
#    main()

