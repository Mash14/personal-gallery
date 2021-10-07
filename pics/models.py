from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    @classmethod
    def update_location(cls,id,new_location):
        cls.objects.filter(id).update(location = new_location)

    @classmethod
    def delete_location(cls,id):
        cls.objects.filter(id).delete() 
