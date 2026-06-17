from django.contrib import admin
from .models import Gallery,Event,Testimonial,AdmissionInquiry,Course

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_on')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'event_date',
        'location'
    )

    search_fields = (
        'title',
        'location'
    )

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        'student_name',
        'designation'
    )

admin.site.register(AdmissionInquiry)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'duration',
        'age_group'
    )

    search_fields = (
        'title',
    )

admin.site.site_header = "Nrityangan Academy Goa"
admin.site.site_title = "Nrityangan Admin"
admin.site.index_title = "Website Management Portal"