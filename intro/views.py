from django.shortcuts import render
from django.http import JsonResponse


# Views for the intro app
def age_form(request):
    """Displaying the age verification form"""
    return render(request, 'intro/index.html')


def age_verification(request):
    """Checking if user is adult: only 18+years old can enter the page"""
    age = request.GET.get('age')
    if age is not None:
        is_adult = int(age) >= 18
        return JsonResponse({'is_adult': is_adult})
    else:
        return JsonResponse({'is_adult': False})
