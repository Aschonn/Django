from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    #if user is deleted the profile will also be, but if profile is deleted user wont be
    #profile is create from signals.py
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # When you are overriding model's save method in Django, you should also pass *args and **kwargs to overridden method. this code may work fine:
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        #open image of instance
        img = Image.open(self.image.path)
        #image can be more than 300px each direction
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


#it automatically includes id
class Feedback(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    comments = models.TextField()

    def __str__(self):
        return self.username