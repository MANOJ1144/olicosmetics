from http import client
from django.test import  TestCase,Client,SimpleTestCase
from django.contrib.auth.models import User
from store.views import store
from django.urls import reverse, resolve

from store.models import Customer

# views testing
class testViews(TestCase):
    def test_store(self):
        user = User.objects.create(username='Manoj')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='Manoj', password='12345')
        response=client.get(reverse('store'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'store\store.html')

    def test_create(self):
        user = User.objects.create(username='Manoj')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='Manoj', password='12345')
        response=client.get(reverse('customer_create'),{
            'first_name':'Manoj',
            'last_name':'Kumar',
            'email':' ',
            'username':'Manoj',
            'password':'12345',            
        })

        self.assertEquals(response.status_code,302)
        self.assertRedirects(response, reverse('store/store'))
    
    def test_cart(self):
        user = User.objects.create(username='Manoj')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='Manoj', password='12345')
        response=client.get(reverse('customer_cart'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'store/cart.html')
    
    def test_checkout(self):
        user = User.objects.create(username='Manoj')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='Manoj', password='12345')
        response=client.get(reverse('checkout'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'store/checkout.html')
    
    def test_homepage(self):
        user = User.objects.create(username='Manoj')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='Manoj', password='12345')
        response=client.get(reverse('homepage'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'store/homepage.html')
    
    def test_login(self):
        user = User.objects.create(username='Manoj')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='Manoj', password='12345')
        response=client.get(reverse('login'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'store/login.html')

    def test_logout(self):
        user = User.objects.create(username='Manoj')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='Manoj', password='12345')
        response=client.get(reverse('logout'))

        self.assertEquals(response.status_code,302)
        self.assertRedirects(response, reverse('login'))

    def test_register(self):
        user = User.objects.create(username='Manoj')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='Manoj', password='12345')
        response=client.get(reverse('register'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'store/register.html')
    
    def test_delete(self):
        client=Client()
        c= Customer.objects.create(
            first_name='Manoj',
            last_name='Kumar',
            email = '',
            username = 'Manoj',
            password = '12345',
        )
        print("this")
        print(c.customer_id)
        response=client.get(reverse('customer_delete',args=[c.customer_id]))

        self.assertEquals(response.status_code,302)