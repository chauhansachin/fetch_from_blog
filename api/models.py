from django.db import models

class Post(models.Model):
    blog_url = models.CharField(max_length=300, unique=True)
    title = models.CharField(max_length=300)
    featured_image = models.CharField(max_length=300)
    content = models.TextField()
    author_name = models.CharField(max_length=300)
    author_image = models.CharField(max_length=300)
    author_bio = models.TextField()
    published_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
