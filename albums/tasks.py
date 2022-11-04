from celery import shared_task

@shared_task(bind=True)
def add(x = 0, y = 0):
    return x + y

@shared_task(bind=True)
def mul(x, y):
    return x * y

