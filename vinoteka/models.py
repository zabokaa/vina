from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Model:
class Diary(models.Model):
    """
    A model representing a diary entry about a wine.

    Fields:
        user (ForeignKey): The user who authored the diary entry. 
            Links to Django's built-in User model.
        wine (CharField): The name of the wine.
        shop (CharField): The shop where the wine was bought.
        day (DateField): The date of the diary entry.
        occasion (CharField): The occasion for which the wine was drunk.
        rating (IntegerField): The rating of the wine, from 1 to 10.
        pic (ImageField): A picture of the wine. Optional.
        memory (TextField): Memories associated with the wine. Optional.
        foodpairing (TextField): The food paired with the wine. Optional.
        again (BooleanField): Whether the user would buy the wine again. Defaults to False.

    The diary entries are ordered by the 'rating' field in ascending order. 
    Each combination of 'user', 'wine', and 'day' must be unique.
"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wine = models.CharField(max_length=200)
    shop = models.CharField(max_length=200)
    day = models.DateField()
    occasion = models.CharField(max_length=200)
    rating = models.IntegerField()
    pic = CloudinaryField('image', blank=True, null=True)
    memory = models.TextField(blank=True, null=True)
    foodpairing = models.TextField(blank=True, null=True)
    again = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "wine", "day")
        ordering = ["rating"]
    def __str__(self):
        return f"{self.user}'s diary entry for {self.wine}"
