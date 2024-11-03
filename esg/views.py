from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from .models import Mentee, Mentor

# Create your views here.

def index(request):
    return render(request, 'index.html')

def mentee(request):
    if request.method == "POST":
        try:
            # Extract data from the request
            first_name = request.POST.get('mentee_first_name')
            last_name = request.POST.get('mentee_last_name')
            email = request.POST.get('mentee_email')
            
            # Validate required fields
            if not first_name or not last_name or not email:
                return JsonResponse({'status': 400, 'message': 'All fields with * are required.'})
            
            mentee_data = {
                'first_name': request.POST.get('mentee_first_name'),
                'last_name': request.POST.get('mentee_last_name'),
                'email': request.POST.get('mentee_email'),
                'age': request.POST.get('mentee_age'),
                'current_education': request.POST.get('current_education'),
                'career_path': request.POST.get('career_path'),
                'industry_interest': request.POST.get('industry_interest'),
                'desired_skill': request.POST.get('desired_skill'),
                'availability': request.POST.get('mentee_availability'),
            }
            Mentee.objects.create(**mentee_data)
            return JsonResponse({'status': 200, 'message': 'Your registration was successful'})
        except ValidationError as e:
            return JsonResponse({'status': 400, 'message': str(e)})
        except Exception as e:
            return JsonResponse({'status': 500, 'message': 'An error occurred: ' + str(e)})

def mentor(request):
    if request.method == "POST":
        try:
            # Extract data from the request
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            
            # Validate required fields
            if not first_name or not last_name or not email:
                return JsonResponse({'status': 400, 'message': 'All fields with * are required.'})

            mentor_data = {
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'email': request.POST.get('email'),
                'age': request.POST.get('age'),
                'current_position': request.POST.get('current_position'),
                'current_industry': request.POST.get('current_industry'),
                'previous_industry_exp': request.POST.get('previous_industry_exp'),
                'areas_of_expertise': request.POST.get('areas_of_expertise'),
                'availability': request.POST.get('availability'),
            }
            Mentor.objects.create(**mentor_data)
            return JsonResponse({'status': 200, 'message': 'Your registration was successful'})
        except ValidationError as e:
            return JsonResponse({'status': 400, 'message': str(e)})
        except Exception as e:
            return JsonResponse({'status': 500, 'message': 'An error occurred: ' + str(e)})
