from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from marketplace.models import Product, PurchasedProduct

# Create your models here.

class User(AbstractUser):
    stripe_customer_id = models.CharField(max_length=50)


class UserLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="library")
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.email


def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
        library=UserLibrary.objects.create(user=instance)

        purchased_products = PurchasedProduct.objects.filter(email=instance.email)

        for purchased_product in purchased_products:
            library.products.add(purchased_product.product)


post_save.connect(post_save_user_receiver, sender=User)