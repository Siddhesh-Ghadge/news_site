from django.db import models

class CustomArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
