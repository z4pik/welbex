from django.db import models

# Create your models here.


class Plan(models.Model):
    the_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    title = models.CharField(max_length=200, verbose_name='Название')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    distance = models.PositiveIntegerField(verbose_name='Расстояние')

    def __str__(self):
        return self.title

