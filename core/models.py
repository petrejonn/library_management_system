from django.db import models
from django.conf import settings
# Create your models here.


class BookCategory(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class LibraryUser(models.Model):
    reg_no = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    other_name = models.CharField(max_length=25)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='department_user')
    photo = models.ImageField(upload_to='uploads')
    phone = models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.other_name


class Book(models.Model):
    title = models.CharField(max_length=25)
    author = models.CharField(max_length=25)
    ISBN = models.CharField(max_length=25)
    copies = models.IntegerField()
    publisher = models.CharField(max_length=25)
    copies_available = models.IntegerField()
    category = models.ForeignKey(
        BookCategory, on_delete=models.CASCADE, related_name='books')
    date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='books')

    def __str__(self):
        return self.title


class Borrow(models.Model):
    STATUS = [('Borrowed', 'Borrowed'), ('Returned', 'Returned')]
    user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE,
                             related_name='borrowed')
    date_issued = models.DateTimeField(auto_now=True)
    date_returned = models.DateTimeField(auto_now_add=True, null=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='borrows')
    status = models.CharField(
        max_length=25, choices=STATUS, default='Borrowed')
    extra_details = models.TextField()
    issuing_staff = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issuing_staff')
    recieving_staff = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recieving_staff', null=True)
    borrow_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.book
