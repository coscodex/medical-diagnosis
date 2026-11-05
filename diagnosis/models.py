from django.db import models

class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptom)
    suggested_medicine = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

