from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=23 , blank=True)

    def __str__(self):
        return f"{self.name}"
