from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RideForm

def home(request):
    if request.method == 'POST':
        # If form is submitted, process the data
        form = RideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after successfully submitting the form
    else:
        form = RideForm()  # Create a new form instance
    return render(request, 'liftclub/home.html', {'form': form})

def select_location(request):
    return render(request, 'liftclub/select_location.html')

def save_location(request):
    if request.method == 'POST':
        # Extract latitude and longitude from the request's JSON payload
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
         # Check if latitude and longitude are present
        if latitude is not None and longitude is not None:
            # Create a new UserLocation object and save it to the database
            user_location = UserLocation(latitude=latitude, longitude=longitude)
            user_location.save()
            
            # Return a JSON response indicating success
            return JsonResponse({'message': 'Location saved successfully'}, status=200)
        else:
            # Return a JSON response indicating missing latitude or longitude
            return JsonResponse({'error': 'Latitude or longitude missing in request'}, status=400)
    else:
        # Return a JSON response indicating failure
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
def visited_locations(request):
    return render(request, 'liftclub/visited_locations.html')

def travels(request):
    return render(request, 'liftclub/travels.csv')

def test(request):
    return render(request, 'liftclub/test.html')