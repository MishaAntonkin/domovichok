from datetime import datetime, timedelta

from celery import Celery, task

from app.config import Config


celery_app = Celery('parser')

#celery_app.config_from_object(Config)
celery_app.conf.update(
    CELERYBEAT_SCHEDULE={
        'now': {
            'task': 'tasks.now',
            'schedule': timedelta(seconds=10)
        },
    }, BROKER_URL="amqp://guest:guest@localhost:5672"
)
from tasks import *
celery_app.autodiscover_tasks()
#print(celery_app.conf)
# to start parser
# celery - A celer worker --beat