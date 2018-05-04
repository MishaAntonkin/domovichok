from datetime import datetime

from celer import celery_app


@celery_app.task
def now():
    with open('asome', 'a+') as f:
        f.write('string\n')
    print(str(datetime.now()))
