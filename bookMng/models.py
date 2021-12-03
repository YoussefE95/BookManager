from django.db import models
from django.contrib.auth.models import User


class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    b_id = models.IntegerField(blank=True, null=True,)
    content = models.TextField(max_length=500)
    publishdate = models.DateField(auto_now=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(max_length=500)
    publishdate = models.DateField(auto_now=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class ShoppingCart(models.Model):
    b_id = models.IntegerField(blank=True, null=True,)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



class WishList(models.Model):
    b_id = models.IntegerField(blank=True, null=True,)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)