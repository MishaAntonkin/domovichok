import requests

from .utils import send_data
from . import app


@app.route('/', methods=['GET', 'POST'])
def index():
    return "success" if send_data(app.config['REST_DB_HOST']) else 'error'