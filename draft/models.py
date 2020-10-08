from django.db import models

# Create your models here.

class Year(models.Model):
    year = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.year

class Player(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    position = models.CharField(max_length=6, null=True)
    college =  models.CharField(max_length=30, null=True)
    height = models.CharField(max_length=4, null=True)
    classof = models.CharField(max_length=6, null=False) 
    position_rank = models.IntegerField()
    year_rank = models.IntegerField(null=False, blank=False)
    player_img = models.ImageField(default='default.jpg', upload_to='player_pics')
    biography = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.name

