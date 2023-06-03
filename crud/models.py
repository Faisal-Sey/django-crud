from django.db import models
from django.forms import model_to_dict


# Create your models here.
class CRUDTestModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

    #  Convert from model instance to dictionary
    def to_dict(self):
        return {"id": self.pk, **model_to_dict(self)}
