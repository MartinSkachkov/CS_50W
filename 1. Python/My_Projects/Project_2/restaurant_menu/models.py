from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starter", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available')
)

# Create your database here.
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(decimal_places=2,max_digits=7)
    category = models.CharField(choices=MEAL_TYPE, max_length=20)
    autor = models.ForeignKey(User, on_delete=models.PROTECT) 
    # CASCADE if the cook is deleted then the meals are also deleted 
    # PROTECT cannot delete the user and then cannot delete the meals
    # SET_NULL if the cook is deleted then the meals will have NULL value for author
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # how the meal will be printed in the admin interface
    def __str__(self):
        return self.meal