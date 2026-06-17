from django.shortcuts import render
from .models import Gallery
from .models import Event,Testimonial,Course
from .forms import AdmissionInquiryForm

def home(request):

    testimonials = Testimonial.objects.all()

    upcoming_events = Event.objects.order_by(
        '-event_date'
    )[:3]

    latest_photos = Gallery.objects.order_by(
        '-uploaded_on'
    )[:6]

    return render(
        request,
        'home.html',
        {
            'testimonials': testimonials,
            'upcoming_events': upcoming_events,
            'latest_photos': latest_photos,
        }
    )

def guru(request):
    return render(request, 'guru.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    courses = Course.objects.all()

    return render(
        request,
        'courses.html',
        {
            'courses': courses
        }
    )

def gallery(request):
    photos = Gallery.objects.all().order_by('-uploaded_on')

    return render(
        request,
        'gallery.html',
        {'photos': photos}
    )


def events(request):

    events = Event.objects.all().order_by(
        '-event_date'
    )

    return render(
        request,
        'events.html',
        {'events': events}
    )
def home(request):

    testimonials = Testimonial.objects.all()

    return render(
        request,
        'home.html',
        {
            'testimonials': testimonials
        }
    )
def contact(request):
    success = False

    if request.method == 'POST':

        form = AdmissionInquiryForm(request.POST)

        if form.is_valid():

            form.save()

            form = AdmissionInquiryForm()

            success = True

    else:

        form = AdmissionInquiryForm()

    return render(
        request,
        'contact.html',
        {
            'form': form,
            'success': success
        }
    )