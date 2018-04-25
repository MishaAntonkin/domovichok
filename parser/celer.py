from datetime import datetime, timedelta

from celery import Celery, task

from config import Config


celery_app = Celery('parser')

#celery_app.config_from_object(Config)
celery_app.conf.update(
    CELERYBEAT_SCHEDULE = {
        'now': {
            'task': 'tasks.now',
            'schedule': timedelta(seconds=10)
        },
    }, BROKER_URL="amqp://guest:guest@localhost:5672"
)

@task
def now():
    print(str(datetime.now()))