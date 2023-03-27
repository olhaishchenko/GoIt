from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Author(models.Model):
    fullname = models.CharField(max_length=250, null=False)
    born_date = models.DateField(null=False)
    born_location = models.CharField(max_length=250, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    tags = ArrayField(models.TextField(max_length=250, null=False))
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    quote = models.TextField(null=False)

    def __str__(self):
        return f"{self.author.fullname}: '{self.quote[:30]}...'"

