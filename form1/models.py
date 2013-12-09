from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField('date of birth')
    gender = models.CharField(max_length=10)
    position = models.CharField(max_length=30)
    def __unicode__(self):
        return self.last_name + ", " + self.first_name

class Contact(models.Model):
    person_id = models.ForeignKey(Person)
    contact_type = models.CharField(max_length=15)
    contact_content = models.CharField(max_length=200)
    start = models.CharField(max_length=15,default="?")
    end = models.CharField(max_length=15, default="?")
    def __unicode__(self):
        return self.contact_content 
                
class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_txt = models.CharField(max_length=30, blank=True)
    def __unicode__(self):
        return self.course_txt
    class Meta:
        app_label = 'sqlite3'   
        db_table = 'course'        