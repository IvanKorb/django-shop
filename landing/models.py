from django.db import models


# Create your models here
class Client(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    # вывод полей в админке
    #def __str__(self):
    #   return "Пользователь: %s Email: %s" % (self.name, self.email)
