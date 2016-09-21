from django.db import models # pragma: no cover


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='books')

    def __unicode__(self):
        return self.name
