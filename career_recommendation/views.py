from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .career_forms import CareerForm
from .recommend import recommend_career
from .models import CareerInput
from django.contrib.auth.decorators import login_required
from .courses_data import courses

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('contact')
    return render(request, 'contact.html')




# Courses page view
@login_required(login_url='/accounts/login/')
def courses_view(request):
    return render(request, 'courses.html', {'courses': courses})
# User dashboard view


@login_required(login_url='/accounts/login/')
def dashboard(request):
   
    # Get 3 most recent recommendations for this user
    recent_recs = CareerInput.objects.filter(name=request.user.username).order_by('-created_at')[:3]
    return render(request, 'dashboard.html', {'recent_recs': recent_recs})


# Show user's past recommendations
@login_required(login_url='/accounts/login/')
def career_history(request):
    history = CareerInput.objects.filter(name=request.user.username).order_by('-created_at')
    return render(request, 'career_history.html', {'history': history})


@login_required(login_url='/accounts/login/')
def recommend_view(request):
    if request.method == 'POST':
        form = CareerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']

            qualification = form.cleaned_data['qualification']
            selected_skill = form.cleaned_data['skills']
            selected_interest = form.cleaned_data['interests']
            # For DB and display, keep as string
            skills = selected_skill
            interests = selected_interest


            # Predict top 3 careers
            # Use recommend_career with single values
            top_careers_raw = recommend_career(qualification, skills, interests)

            # Map career names to local image filenames (add your own mappings as needed)
            career_image_map = {
                'Software Developer': 'software_developer.jpg',
                'Data Analyst': 'data_analyst.jpg',
                'Digital Marketer': 'digital_marketer.jpg',
                'Business Analyst': 'business_analyst.jpg',
                'UX Researcher': 'ux_researcher.jpg',
                'AI Specialist': 'ai_specialist.jpg',
                'Graphic Designer': 'graphic_designer.jpg',
                'Data Scientist': 'data_scientist.jpg',
                'Project Manager': 'project_manager.jpg',
                'Deep Learning Engineer': 'deep_learning_engineer.jpg',
                'Cloud Engineer': 'cloud_engineer.jpg',
                'Machine Learning Engineer': 'machine_learning_engineer.jpg',
                'UX Designer': 'ux_designer.jpg',
                # Add more mappings as needed
            }

            # Build list of (career, score, image_url)
            top_careers = []
            for career, score in top_careers_raw:
                image_file = career_image_map.get(career, 'default.jpg')
                image_url = f'../static/career_images/{image_file}'
                top_careers.append((career, score, image_url))

            # Save in DB
            CareerInput.objects.create(
                name=name,
                age=age,
                education=qualification,
                skills=skills,
                interest=interests,
                predicted_career=top_careers[0][0]  # top career name
            )

            return render(request, 'recommend.html', {
                'name': name,
                'age': age,
                'qualification': qualification,
                'skills': skills,
                'interests': interests,
                'top_careers': top_careers
            })
    else:
        form = CareerForm()

    return render(request, 'career_form.html', {'form': form})

def career_history(request):
    searchTerm=request.GET.get('searchcareer')
    if searchTerm:
        user_history=CareerInput.objects.filter(predicted_career__icontains=searchTerm)
        return render(request,'career_history.html',{'history':user_history})
      
    if request.user.is_authenticated:
            user_history = CareerInput.objects.all().order_by('-created_at').filter(name=request.user.username)
            return render(request, 'career_history.html', {'history': user_history})
    else:
            user_history = []
            return render(request, 'career_history.html', {'history': user_history})