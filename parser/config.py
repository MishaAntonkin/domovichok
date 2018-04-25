from celery.schedules import crontab


class Config(object):
    SECRET_KEY = 'you-will-never-guess'
    CELERYBEAT_SCHEDULE = {'some': {'task': 'tasks.X_Y', 'schedule': crontab(minute="*/1")}, }
    BROKER_URL = "amqp://guest:guest@localhost:5672"
    CELERYBEAT_MAX_LOOP_INTERVAL = 30

REST_DB_HOST = 'http://127.0.0.1:8001'

