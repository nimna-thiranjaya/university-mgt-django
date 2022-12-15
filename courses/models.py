from django.db import models


# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_no = models.CharField(max_length=4)
    course_name = models.CharField(max_length=200)
    course_weight = models.IntegerField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
