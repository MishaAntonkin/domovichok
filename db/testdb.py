import random
import re

import requests

test_data = [{'name': 'ул. Болсуновская, 2', 'price': '2 800 $', 'area': '87 м²'},
             {'name': 'ул. Шепелева Николая, 13', 'price': '6 000 грн', 'area': '40 / 18 / 9 м²'},
             {'name': 'бульвар Дружбы Народов', 'price': '800 $', 'area': '85 м²'},
             {'name': 'ул. Драгомирова, 2а', 'price': '700 $', 'area': '75 м²'},
             {'name': 'ул. Коновальца, 44а', 'price': '800 $', 'area': '68 м²'},
             {'name': 'ул. Урловская, 38', 'price': '12 500 грн', 'area': '67 м²'},
             {'name': 'ул. Бакинская, 37', 'price': '10 000 грн', 'area': '48 м²'},
             {'name': 'просп. Петра Григоренко, 1', 'price': '8 200 грн', 'area': '46 / 18.1 / 10.1 м²'},
             {'name': 'ул. Владимирская, 82', 'price': '12 000 грн', 'area': '50 / 18 / 10 м²'},
             {'name': 'ул. Северная, 18', 'price': '8 000 грн', 'area': '34 / 18 / 7 м²'},
             {'name': 'ул. Януша Корчака, 64', 'price': '6 200 грн', 'area': '36 / 18 / 8.5 м²'},
             {'name': 'ул. Срибнокильская, 2', 'price': '4 500 грн', 'area': '43 / 18 / 9 м²'},
             {'name': 'ул. Курчатова Академика, 3а', 'price': '4 000 грн', 'area': '60 / 35 / 7 м²'},
             {'name': 'Деснянский, Киевская область', 'price': '6 500 грн', 'area': '50 м²'},
             {'name': 'пр. Победы', 'price': '8 000 грн', 'area': '50 м²'},
             {'name': 'ул. Сергея Данченко, 1', 'price': '8 500 грн', 'area': '49 / 17 / 13 м²'},
             {'name': 'ул. Сечевых Стрельцов, 70а', 'price': '2 000 $', 'area': '130 м²'},
             {'name': 'ул. Елизаветы Чавдар, 34', 'price': '13 000 грн', 'area': '56 м²'},
             {'name': 'ул. Братьев Зеровых, 14б', 'price': '1 000 €', 'area': '131 / 89 / 15 м²'},
             {'name': 'Днепровская набережная, 14', 'price': '15 500 грн', 'area': '57 м²'},
             {'name': 'ул. Ломоносова, 31', 'price': '6 500 грн', 'area': '42 м²'},
             {'name': 'ул. Златоустовская', 'price': '16 000 грн', 'area': '54 / 32 / 16 м²'},
             {'name': 'ул. Пушкинская, 31а', 'price': '2 000 $', 'area': '109 / 57 / 9 м²'},
             {'name': 'ул. Строителей, 12', 'price': '7 000 грн', 'area': '30 м²'},
             {'name': 'Аренда 1 комнатной квартиры, люкс', 'price': '6 500 грн', 'area': '50 м²'},
             {'name': 'ул. Верховинная, 35', 'price': '12 000 грн', 'area': '81 / 41 / 15 м²'},
             {'name': 'ул. Иорданская, 11б', 'price': '9 000 грн', 'area': '50 / 38 / 9 м²'},
             {'name': 'ул. Деревлянская, 16', 'price': '11 000 грн', 'area': '52 / 30 / 15 м²'},
             {'name': 'ул. Петра Куренного, 3', 'price': '6 000 грн', 'area': '44 / 29 / 8 м²'},
             {'name': 'ул. Златоустовская, 34', 'price': '15 000 грн', 'area': '50 / 35 / 15 м²'}]


def test_save_houses():
    """
    /houses/ POST
    test to save multiple houses
    """
    #test 1
    data = [{'name': "text", 'district': "Dnipr", 'price': '12.94'},{'name': "text", 'district': "Dnipr", 'price': '120.94'}]
    r = requests.post('http://127.0.0.1:8001/houses/', json=data)
    print(r.status_code)
    print(r.json())


    #test 2
    data = {'name': "text", 'district': "Dnipr", 'price': '12.94'}
    r = requests.post('http://127.0.0.1:8001/houses/', json=data)
    print(r.status_code)
    print(r.json())


def test_get_houses():
    """
    /houses/ GET
    test to get all availables houses
    """
    r = requests.get('http://127.0.0.1:8001/houses/')
    print(r.status_code)
    print(r.json())


def test_get_house():
    """
    /houses/ GET
    test to get all availables houses
    """
    r = requests.get('http://127.0.0.1:8001/houses/1/')
    print(r.status_code)
    print(r.json())


def test_delete_house():
    """
    /houses/<int:id>/ DELETE
    test to delete object
    """
    r = requests.delete('http://127.0.0.1:8001/houses/1/')
    print(r.status_code)
    if r.headers.get('content-type') == 'application/json':
        print(r.json())


def test_update_house():
    """
        /houses/<int:id>/ PUT
        test to update object
        """
    price = random.randint(0, 100)
    r = requests.put('http://127.0.0.1:8001/houses/1/', json={'price': price})
    print(r.status_code)
    print(r.json())


#test_save_houses()
#test_get_houses()
#test_get_house()
#test_delete_house()
#test_update_house()

def chunk_generator(data, piece):
    if not data:
        raise Exception('no data to slice')
    elif piece < 1:
        raise Exception('no sence to slice')
    for i, inx in enumerate(data[::piece]):
        yield data[i*piece:(i+1)*(piece)]

list1 = list(range(109))

list2 = chunk_generator(list1, 20)
#list1[20:112] = [1,23,4,6,7]
for inx in list2:
    print(inx)
#print(list1)