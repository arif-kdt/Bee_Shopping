from django.db import models

class Grocery(models.Model):

    TYPE_CHOICE = [
        ('FRUITS', 'Fruits'),
        ('VEGETABLES', 'Vegetables'),
    ]

    name = models.CharField(unique=True)
    type = models.CharField(choices=TYPE_CHOICE, default='FRUITS')
    image = models.ImageField(upload_to='Groceries/')


    def __str__(self):
        return self.name