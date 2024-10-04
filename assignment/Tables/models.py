from django.db import models

# Create your models here.
# Create your models here.
class Answers(models.Model):
    Id = models.AutoField(primary_key=True)
    Answers = models.CharField(max_length=1)

# Create your models here.
class Assessment_Areas(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

class Awards(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Class(models.Model):

    Id = models.AutoField(primary_key=True)
    Class= models.CharField(max_length=255)

class School(models.Model):

    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    Id = models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=255)

class Subject(models.Model):
    Id = models.AutoField(primary_key=True)
    Subject = models.CharField(max_length=255)
    Subject_score = models.FloatField()

class Summary(models.Model):

    School_Id = models.IntegerField()
    Sydney_Participant = models.IntegerField()
    Sydney_Percentile = models.DecimalField(max_digits=5,decimal_places=2)
    Assesment_Area_Id = models.IntegerField()
    Award_Id = models.IntegerField()
    Class_Id = models.IntegerField()
    Correct_answer_percentage_per_class = models.DecimalField(max_digits=5,decimal_places=2)
    Correct_Answer = models.CharField(max_length=1)
    Student_Id = models.IntegerField()
    Participant =  models.IntegerField()
    Student_score = models.DecimalField(max_digits=5,decimal_places=2)
    Subject_Id = models.IntegerField()
    Category_Id = models.IntegerField()
    year_level_name = models.IntegerField()
    Answer_Id = models.IntegerField()
    Correct_answer_Id = models.IntegerField() 

    def __str__(self):
        return f"Summary for Student ID {self.Student_Id}"  