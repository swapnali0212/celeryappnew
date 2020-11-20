from newapp.celery import app
from appone.models import Tasks
from time import sleep
import random


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

