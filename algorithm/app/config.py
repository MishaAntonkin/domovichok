import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'you-will-never-guess'
    POSTS_PER_PAGE = 20
    INTERFACE_ADDRESS = 'http://127.0.0.1:8000'
    DB_ADDRESS = 'http://127.0.0.1:8001'
    WHITE_LIST = ['127.0.0.1']
