from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import uuid

# Create your models here.

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    mobile_phone = models.fields.CharField(max_length=50)
    upload = models.FileField(upload_to='uploads/')


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.fields.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.ForeignKey(
        Country,
        related_name='cities',
        on_delete=models.CASCADE,
    )
    name = models.fields.CharField(max_length=100)

    def __str__(self):
        return self.name


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )
    address = models.fields.CharField(max_length=300)
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return '{} - {}'.format(self.address, self.city)



# TODO Refactor models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=300)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=300)

    amount = models.fields.PositiveIntegerField()
    stock = models.fields.PositiveIntegerField()

    active = models.fields.BooleanField(default=True)

    def __str__(self):
        return self.name


class Imagen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    upload = models.FileField(upload_to='media/')
    name = models.fields.CharField(max_length=100)
    active = models.fields.BooleanField(default=True)




class Buy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
    )

