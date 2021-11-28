from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)

    def __str__(self):
        return self.title
