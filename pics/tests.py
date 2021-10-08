from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.

class LocationTestCase(TestCase):

    #setUp method
    def setUp(self):
        self.new_location = Location(location = 'Nairobi')

    # tearDown method
    def tearDown(self):
        Location.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    # Testing instance variables
    def test_check_instance_variables(self):
        self.assertEquals(self.new_location.location, 'Nairobi')

    # Test Save Method
    def test_save_method(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    # Test update method
    def test_update_method(self):
        self.new_location.save_location()
        location_id = self.new_location.id
        Location.update_location(location_id, 'Mombasa')
        self.assertEquals(self.new_location.location, 'Mombasa')

    # Test delete method
    def test_delete_method(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class CategoryTestClass(TestCase):

    #setUp method
    def setUp(self):
        self.new_category = Category(category = 'Travel')

    # tearDown method
    def tearDown(self):
        Category.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category, Category))

    # Testing instance variables
    def test_check_instance_variables(self):
        self.assertEquals(self.new_category.category, 'Travel')

    # Test Save Method
    def test_save_method(self):
        self.new_category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    # Test update method
    def test_update_method(self):
        self.new_category.save_category()
        category_id = self.new_category.id
        Category.update_category(category_id, 'Food')
        self.assertEquals(self.new_category.category, 'Food')

    # Test delete method
    def test_delete_method(self):
        self.new_category.save_category()
        category_id = self.new_category.id
        self.new_category.delete_category(category_id)
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)


class ImageTestClass(TestCase):

    # setUp method
    def setUp(self):
        # Create a new location and save it
        self.new_location = Location(location = 'Nairobi')
        self.new_location.save_location()

        # Create a new category and save it
        self.new_category = Category(category = 'Food')
        self.new_category.save_category()

        # Create a new Image and save it
        self.new_image = Image(image = 'image2.jpg',image_url = 'http://wallpaperstone.blogspot.com/2007/09/view-wallpaper-in-room.html', image_name = 'wallpaper', image_description = 'test wallpaper',image_location = self.new_location, image_category = self.new_category)
        self.new_image.save_image()

    # teardown method
    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    # Test Save Method
    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # Test the updating method
    def test_update_method(self):
        self.new_image.save_image()
        image_id = self.new_image.id
        Image.update_image(image_id,'image12.jpg')
        self.assertTrue(self.new_image.image_name,'image12.jpg')

    # Test the get image by id method
    def test_get_image_by_id(self):
        self.new_image.save_image()
        search_image = self.new_image.get_image_by_id(self.new_image.id)
        searched_image = Image.objects.filter(id=self.new_image.id)
        self.assertTrue(searched_image,search_image)

    # Test the search by category method
    def test_search_by_category(self):
        self.new_image.save_image()
        category = 1
        searched_image = self.new_image.search_by_category(category)
        self.assertTrue(len(searched_image)>0)

    # Test the filter by category method
    def test_filter_by_location(self):
        self.new_image.save_image()
        location = 1
        searched_image = self.new_image.filter_by_location(location)
        self.assertTrue(len(searched_image) > 0)

    # Test the delete method
    def test_delete_image(self):
        self.new_image.save_image()
        self.new_image.delete_image(id = self.new_image.id)
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

