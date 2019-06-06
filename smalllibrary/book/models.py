from django.db import models

# Create your models here.
class Borrow(models.Model):
    borrower = models.CharField(max_length=255)  

    def __str__(self):
        return self.borrower

class Publisher(models.Model):
    publish_name = models.CharField(max_length=255)

    def __str__(self):
        return self.publish_name

class Binding(models.Model):
    biding_name = models.CharField(max_length=255)
    def __str__(self):
        return self.biding_name
class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    biding = models.ForeignKey(Binding,on_delete=models.SET_NULL,null=True)    
    year = models.PositiveSmallIntegerField()
    publish = models.ForeignKey(Publisher,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    actor = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book


