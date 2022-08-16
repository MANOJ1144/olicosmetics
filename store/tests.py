from django.test import  SimpleTestCase, TestCase
from django.urls import reverse, resolve
from store.views import store, cart, checkout, homepage

# url testing
class  TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('store')
        print(url)
        self.assertEquals(resolve(url).func,store)

    def test_index_url(self):
        url = reverse('customer_cart')
        print(url)
        self.assertEquals(resolve(url).func,cart)

    def test_index_url(self):
        url = reverse('checkout')
        print(url)
        self.assertEquals(resolve(url).func,checkout)

    def test_index_url(self):
        url = reverse('homepage')
        print(url)
        self.assertEquals(resolve(url).func,homepage)


    
   
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "store/homepage.html")

    def test_template_content(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, "<h1>homepage</h1>")
        self.assertNotContains(response, "Not on the page")


class CartPageTests(SimpleTestCase):  # new
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("cart"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("cart"))
        self.assertTemplateUsed(response, "store/cart.html")

    def test_template_content(self):
        response = self.client.get(reverse("cart"))
        self.assertContains(response, "<h1>Cart page</h1>")
        self.assertNotContains(response, "Should not be here!")

