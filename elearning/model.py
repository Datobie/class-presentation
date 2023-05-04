from django.db import models

# Create your models here.


class Hero_section(models.Model):
    name = models.CharField(max_length=300)
    topic = models.CharField(max_length=300)
    description = models.TextField(max_length=800)
    image = models.ImageField(upload_to="hero-images")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Hero_sections"


class Service(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
class About(models.Model):
    image = models.ImageField(upload_to="about_images")
    name = models.CharField(max_length= 300)
    topic = models.CharField(max_length=200)
    description_1 = models.TextField(max_length=600)
    description_2 = models.TextField(max_length=600)
    about1 = models.CharField(max_length=200)
    about2 = models.CharField(max_length=200)
    about3 = models.CharField(max_length=200)
    about4 = models.CharField(max_length=200)
    about5 = models.CharField(max_length=200)
    about6 = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name
    

class Course_category(models.Model):
    image = models.ImageField(upload_to="course_images")
    description = models.CharField(max_length=100)
    course_amount = models.CharField(max_length=200)


    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural = "Course_categories"

class Popular_courses(models.Model):
    image = models.ImageField(upload_to="Popular_images")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    duration = models.TextField(max_length=100)
    students = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "Popular_courses"


class Instructor(models.Model):
    image = models.ImageField(upload_to="instructor_images")
    name = models.CharField(max_length=300)
    designation = models.CharField(max_length=200)

    
    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial_images")
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    content = models.TextField(max_length=300)

    def __str__(self):
        return self.name
    

class contactPage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    address = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to="contact_images")

    def __str__(self):
        return self.name
    
class formSection(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=400)
    message = models.TextField()



# class Footer_category(models.Model):
#     links = models.CharField(max_length=300)
#     contact = models.CharField()
#     images = models.ImageField()


