# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
from django.db import models
# # Create your models here.
# #
class FoodDay(models.Model):
    class Meta:
        db_table = "food_day"
    foodDay = models.TextField()
    foodDayNumber = models.IntegerField(default=1)
    def __str__(self):
        return self.foodDay


class Menu(models.Model):
    class Meta:
        db_table = "menu"
    categoryName = models.TextField()
    categoryPrice = models.FloatField()
    def __str__(self):
        return self.categoryName
    def __unicode__(self):
        return self.categoryName




class FoodsCustom(models.Model):
    class Meta:
        db_table = "foods_custom"
    customUserName = models.TextField()
    customFirstName = models.TextField()
    customLastName = models.TextField()
    firstFood = models.TextField()
    garnish = models.TextField()
    salad = models.TextField()
    meatDish = models.TextField()
    fruits = models.TextField()
    complex = models.TextField()
    customDate = models.DateField()
    dinnerDate = models.DateField()
    customPrice = models.FloatField()
    paymentFood = models.TextField()
    def __unicode__(self):
        return "{0}, {1}".format(self.customFirstName, self.customLastName, self.firstFood,self.garnish,self.salad,self.meatDish, self.fruits,self.complex,self.paymentFood)

    def __str__(self):
        return self.customUserName


class Eating(models.Model):
    class Meta:
        db_table = "eating"
    foodName = models.TextField()
    foodDescriptions = models.TextField()
    foodImage = models.TextField(default=None)
    foodCategory = models.ForeignKey(Menu)
    foodDay = models.ForeignKey(FoodDay)
    def __unicode__(self):
        return "{0}, {1}".format(self.foodName, self.foodDescriptions)

    def __str__(self):
        return self.foodName