from django.db import models

# Create your models here.

# Tạo models

from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass

class BaseModel(models.Model):
    create_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null = True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Courses(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    # description = models.TextField()
    description = RichTextField()
    # image = models.CharField(max_length=100)
    image =models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'category')

class Lesson(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    # content = models.TextField()
    content = RichTextField()
    image = models.ImageField(upload_to='lessons/%Y/%m')
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    class Meta:
        unique_together = ('subject', 'courses')

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name