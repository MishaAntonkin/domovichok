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


def get_price(bsObj):
    price = bsObj.findAll("div", {"class": "realty-card-characteristics__price"})

    return price[0].get_text()


def get_area(bsObj):
    area = bsObj.findAll("div", {"class": "realty-card-characteristics-list__item"})

    # Ждем исключения, если не указана площадь.
    try:
        return area[1].get_text()
    except IndexError as ae:
        return "Информация не найдена"


def get_data_from_page(bsObj, data):
    """
    Получаем данные с конкретной страницы
    """
    for house_info in bsObj.findAll("div", {"class": "realty-card-inner"}):
        house_data = {"name": get_name(house_info), "price": get_price(house_info),
                      "area": get_area(house_info)}

        data.append(house_data)

    return data


def check_next_page_exist(bsObj):
    """
    Проверяем есть ли следующая страница
    """
    if bsObj.find("i", {"class": "icon-right-open"}):
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

        if page_number == 2:
            return data

        print("Существует страница №", page_number)
        print("Сканирем страницу №", page_number)
        bsObj = BeautifulSoup(get_html(page_number), "html.parser")
        get_data_from_page(bsObj, data)

    return data


def parse_data():
    data = get_data()
    return data

#if __name__ == '__main__':
#    main()

