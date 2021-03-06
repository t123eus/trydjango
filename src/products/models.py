from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	title 		= models.CharField(max_length=120)
	description = models.TextField(blank=False, null=True)
	price 		= models.DecimalField(decimal_places=2, max_digits=10000)
	summary		= models.TextField()
	featured    = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse("products_namespace:product-detail", kwargs={"id": self.id})
		#return f"/products/{self.id}/"

	def get_product_detail_url(self):
		return reverse("products_namespace:product-list")