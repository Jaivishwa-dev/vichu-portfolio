
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse

from .models import Project, Skill, Testimonial

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    testimonials = Testimonial.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send an email
        send_mail(
            f'New Contact Form Submission from {name}',
            f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}',
            email,
            ['jaivishwa.dev@gmail.com'],  # Replace with your email
            fail_silently=False,
        )

        # Respond with a success message (JSON response for AJAX)
        return JsonResponse({'message': 'Thank you for your message. I will get back to you soon.'})

    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'skills': skills,
        'testimonials': testimonials
    })


from django.shortcuts import render
from django.http import FileResponse, Http404

def showcaseing_my_resume(request):
    try:
        # Path to the resume file
        resume_path = 'static/resume/jaivishwa.dev.pdf'  # Update with the correct path
        return FileResponse(open(resume_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404("Resume not found.")



