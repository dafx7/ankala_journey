from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    photo1 = models.ImageField(upload_to='articles/')
    photo2 = models.ImageField(upload_to='articles/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='articles/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='articles/', blank=True, null=True)
    photo5 = models.ImageField(upload_to='articles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
