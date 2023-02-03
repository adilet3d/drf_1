from django.db import models

from django.contrib.auth.models import AbstractBaseUser

class Courses(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя курса')
    description= models.CharField(max_length=120, verbose_name='Описание')
    start_date= models.DateField(verbose_name='Дата начала')

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name= "Курс"
        verbose_name_plural= "Курсы"

