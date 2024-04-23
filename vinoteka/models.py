from django.db import models
from django.contrib.auth.models import User

# Model:
class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wine = models.CharField(max_length=200)
    shop = models.CharField(max_length=200)
    day = models.DateField()
    occasion = models.CharField(max_length=200)
    rating = models.IntegerField()
    pic = models.ImageField(upload_to='diary_pics/', blank=True, null=True)
    memory = models.TextField(blank=True, null=True)
    foodpairing = models.TextField(blank=True, null=True)
    again = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "wine", "day")
        ordering = ["rating"]


    def __str__(self):
        return f"{self.user}'s diary entry for {self.wine}"