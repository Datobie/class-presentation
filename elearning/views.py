from django.shortcuts import render
from django.http import HttpResponse
from .model import Hero_section, Service, About, Course_category, Popular_courses, Instructor, Testimonial, contactPage, formSection
from .forms import contactForm


def home_page(request):
    hero_category = Hero_section.objects.all()
    service_category = Service.objects.all()
    about_category = About.objects.all()
    course_section = Course_category.objects.all()
    popular_courses = Popular_courses.objects.all()
    instructor = Instructor.objects.all()
    testimonial = Testimonial.objects.all()
    # footer_category = Footer_category.objects.all()

    context = {
        "hero_category": hero_category,
        "service_category": service_category,
        "about_category": about_category,
        "course_section": course_section,
        "popular_courses": popular_courses,
        "instructor": instructor,
        "testimonial": testimonial
    }
    return render(request, "elearning/index.html", context)


def about_page(request):
    service  = Service.objects.all()
    about = About.objects.all()
    instructor = Instructor.objects.all()

    context = {
        "service": service,
        "about": about,
        "instructor": instructor
    }

    return render(request, "elearning/about.html", context)


def course_page(request):
    course = Course_category.objects.all()
    pop_courses = Popular_courses.objects.all()
    course_testimonial = Testimonial.objects.all()

    context = {
        "course": course,
        "pop_courses": pop_courses,
        "course_testimonial": course_testimonial
    }
    return render(request, "elearning/courses.html", context)


def Contact(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you!")
        
    else:
        contact = contactPage.objects.all()
        c_forms = formSection.objects.all()
        

    context = {
        "contact": contact,
        "c_forms": c_forms,
        # "form": form
    }

    return render(request, 'elearning/contact.html', context)

