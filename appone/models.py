from django.db import models


class Tasks(models.Model):
    task_id = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    item_status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.task_id} {self.item_name} {self.item_status}'
