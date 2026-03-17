from django.db import models

class Students_Reg(models.Model):
    Name = models.CharField(max_length=15)
    Enrollment_no = models.CharField(max_length=15)
    Roll_no = models.IntegerField()
    Email =models.EmailField(unique=True)
    Password = models.CharField(max_length=12,unique=True)


class Subject_log(models.Model):
    Date_Time = models.DateTimeField()
    Name = models.CharField(max_length=15)
    Enrollment_no = models.IntegerField()


class Class_data(models.Model):
    Date_Time = models.DateTimeField()
    Teacher_Name = models.CharField(max_length=15)


class Student_Attendance(models.Model):
    Roll_no = models.CharField(max_length=10)
    Teacher_name = models.CharField(max_length=30)
    Subject_name = models.CharField(max_length=30)
    Subject_Location = models.CharField(max_length=255)
