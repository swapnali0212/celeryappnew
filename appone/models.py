from django.db import models


class Tasks(models.Model):
    task_id = models.IntegerField('item_id')
    item_name = models.CharField('item_name',max_length=50)
    item_status = models.CharField('item_status', max_length=50)

    def __str__(self):
        return f'{self.task_id} {self.item_name} {self.item_status}'
