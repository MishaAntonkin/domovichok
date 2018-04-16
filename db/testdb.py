import random

import requests


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

test_save_houses()
test_get_houses()
test_get_house()
test_delete_house()
#test_update_house()