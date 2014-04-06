from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Ingredient(models.Model):
    dish = models.ForeignKey(Dish)
    ingredient = models.CharField(max_length=30)
    amount = models.IntegerField(default=0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.ingredient