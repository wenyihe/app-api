from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='test@gmail.com',password = 'passtest'):
    """Create a samaple user"""
    return get_user_model().objects.create_user(email,password)

class ModeTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gamil.com'
        password = 'pass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_email_normalized(self):
        """test the email for the new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())

    def test_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    
    def test_creat_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag(self):
        """Test the tag as string"""
        tag = models.Tag.objects.create(
            user = sample_user(),
            name = 'Vegan'

        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient(self):
        """Test the ingredient as string"""
        ingredient = models.Ingredient.objects.create(
            user = sample_user(),
            name = 'Eggs'

        )
        self.assertEqual(str(ingredient), ingredient.name) 

    def test_recipe(self):
        """Test the recipe as string"""
        recipe = models.Recipe.objects.create(
            user = sample_user(),
            name = 'Steak',
            time = 5,
            price = 10,
        )
        self.assertEqual(str(recipe), recipe.name)  
        

    