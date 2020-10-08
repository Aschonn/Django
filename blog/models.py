
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    #describe how results will be printed out
    # Before: <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>
    # After: <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>`


    #reverse: return full url as a string
    #pk=primary key


#NOTES:
# get all objects
# I believe it's exactly like query in flask
# Post.objects.all()

# the benefits of django is the ability to grab info easily 
# post = Post.objects.first()
# post.content
# result = 'First Post Content!' 

#create a post from user post_set 
# this method doesnt require author because the author is the user that is in the command
# user.post_set.create(title='Blog3', content='Third post content')