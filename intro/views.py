from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def age_form(request):
    return render(request, 'intro/age_verification.html')

def age_verification(request):
    age = request.GET.get('age')
    if age is not None:
        is_adult = int(age) >= 18
        return JsonResponse({'is_adult': is_adult})
    else:
        return JsonResponse({'is_adult': False})
