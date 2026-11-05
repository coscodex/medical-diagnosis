from django.shortcuts import render
from .models import Disease, Symptom  # Ensure you import your models

def home(request):
    return render(request, 'home.html')

def diagnose(request):
    # Fetch all symptoms to populate the selection in the form
    symptoms = Symptom.objects.all()
    
    if request.method == 'POST':
        # Retrieve selected symptom IDs from the form submission
        symptom_ids = [
            request.POST.get('symptom1'),
            request.POST.get('symptom2'),
            request.POST.get('symptom3'),
            request.POST.get('symptom4')
        ]
        # Convert to integer and filter out any empty values
        symptom_ids = [int(sid) for sid in symptom_ids if sid]

        # Query for diseases associated with the selected symptoms
        diseases = Disease.objects.filter(symptoms__id__in=symptom_ids).distinct()

        context = {
            'diseases': diseases,
            'symptom_ids': symptom_ids,
        }
        return render(request, 'result.html', context)

    context = {
        'symptoms': symptoms,  # Pass the list of symptoms to the template
    }
    return render(request, 'diagnose.html', context)

def result(request):
    # This function is no longer needed since `diagnose` handles the result logic
    return render(request, 'diagnose.html')  # Redirect to diagnose if accessed directly




