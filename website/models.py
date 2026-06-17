from django.db import models

class Gallery(models.Model):

    CATEGORY_CHOICES = [
        ('Performance', 'Performance'),
        ('Workshop', 'Workshop'),
        ('Competition', 'Competition'),
        ('Arangetram', 'Arangetram'),
        ('Event', 'Event'),
        ('Award', 'Award'),
    ]

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Performance'
    )

    image = models.ImageField(upload_to='gallery/')

    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Event(models.Model):

    title = models.CharField(max_length=200)

    event_date = models.DateField()

    location = models.CharField(
        max_length=200,
        blank=True
    )

    image = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class Testimonial(models.Model):

    student_name = models.CharField(max_length=100)

    photo = models.ImageField(
        upload_to='testimonials/',
        blank=True,
        null=True
    )

    message = models.TextField()

    designation = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.student_name
    
class AdmissionInquiry(models.Model):

    student_name = models.CharField(max_length=100)

    parent_name = models.CharField(
        max_length=100,
        blank=True
    )

    age = models.IntegerField()

    mobile = models.CharField(max_length=15)

    email = models.EmailField(blank=True)

    course = models.CharField(max_length=100)

    message = models.TextField(blank=True)

    submitted_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.student_name
    
class SocialMedia(models.Model):

    facebook = models.URLField(blank=True)

    instagram = models.URLField(blank=True)

    youtube = models.URLField(blank=True)

    def __str__(self):
        return "Social Media Links"
class Course(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='courses/',
        blank=True,
        null=True
    )

    duration = models.CharField(
        max_length=100
    )

    age_group = models.CharField(
        max_length=100,
        blank=True
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title