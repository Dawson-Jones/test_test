import time
from celery import Celery

celery = Celery("tasks", broker="redis://localhost:6379/0")


@celery.task
def send_mail(a, b):
    print("a + b = %d..." % (a + b))
    time.sleep(2.0)
    print("finish.")


if __name__ == '__main__':
    send_mail.delay(2, 3)
