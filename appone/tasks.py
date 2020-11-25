from newapp.celery import app
from appone.models import Tasks
from time import sleep
from celery import shared_task
import random



@app.task
def add(x, y):
    return x / y

@app.task(bind=True)
def process(self, item_name=None, item_status=None):

    b = Tasks(task_id=self.request.id, item_name=item_name, item_status=item_status)
    b.save()

    self.update_state(state='started', meta={'progress': '33'})
    sleep(random.randint(5, 10))

    self.update_state(state='pending', meta={'progress': '66'})
    sleep(random.randint(5, 10))

    self.update_state(state='completed', meta={'progress': '100'})
    sleep(random.randint(5, 10))

