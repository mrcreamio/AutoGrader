from django.db import models
# Create your models here.
class home_student_record(models.Model):
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    rollno=models.CharField(max_length=50)



class home_teacher_record(models.Model):
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=50)
   
class course(models.Model):
    teacher_id=models.ForeignKey('home_teacher_record',on_delete=models.CASCADE)
    credit_hours=models.CharField(max_length=20)
    course_name=models.CharField(max_length=20)
    code=models.IntegerField(primary_key=True)



class uploaded_files(models.Model):
    course_no = models.ForeignKey('course',on_delete=models.CASCADE)
    zipfile = models.FileField(upload_to='assignments/pdf/')
    
   
    def __str__(self):
       return str(self.zipfile.name)
    def get_download_url(self):
        return self.zipfile.url
    @property
    def name(self):
        return self.zipfile.name

class course_registered(models.Model):
    student_id=models.ForeignKey('home_student_record',on_delete=models.CASCADE)
    course_id=models.ForeignKey('course',on_delete=models.CASCADE)


class score(models.Model):
    student_id=models.ForeignKey('home_student_record',on_delete=models.CASCADE)
    assign_name=models.CharField(max_length=50)
    assign_number=models.IntegerField()
    passed = models.IntegerField()
    failed = models.IntegerField()
    total = models.IntegerField(null=True)
    obtainedMarks = models.IntegerField(null=True)
