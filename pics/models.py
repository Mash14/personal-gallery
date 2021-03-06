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
        cls.objects.filter(id = id).update(location = new_location)

    @classmethod
    def delete_location(cls,id):
        cls.objects.filter(id = id).delete() 


class Category(models.Model):
    category = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    @classmethod
    def update_category(cls,id,new_category):
        cls.objects.filter(id = id).update(category = new_category)

    @classmethod
    def delete_category(cls,id):
        cls.objects.filter(id = id).delete()


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_url = models.TextField(blank = True)
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    @classmethod
    def image_list(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def update_image(cls,id,new_image):
        cls.objects.filter(id = id).update(image_name = new_image)

    @classmethod
    def get_image_by_id(cls,id):
        images = cls.objects.get(id = id)
        return images

    @classmethod
    def search_by_category(cls,searched_category):
        images = cls.objects.filter(image_category__category__icontains = searched_category)
        return images

    @classmethod
    def filter_by_location(cls,searched_location):
        images = cls.objects.filter(image_location__location__icontains = searched_location)
        return images

    @classmethod
    def delete_image(cls,id):
        cls.objects.filter(id = id).delete()
