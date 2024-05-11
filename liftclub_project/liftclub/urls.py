from django.urls import path
from django.http import FileResponse
from liftclub.views import home # Import the home view from liftclub.views
from . import views

urlpatterns = [
    # Map the home view to the root URL: This means that when users visit the root URL of your app (e.g., http://127.0.0.1:8000/), they will see the home page rendered by the home view.
    path('', home, name='home'),  # Map the home view to the root URL

    # URL route for viewing travels
    path('visited-locations/', views.visited_locations, name='visited_locations'),

    # URL route for selecting a location
    path('select-location/', views.select_location, name='select_location'),
    
    # URL route for saving a location
    path('save-location/', views.save_location, name='save_location'),

     # Serve the travels.csv file directly
    path('travels.csv', lambda request: FileResponse(open('liftclub/templates/liftclub/travels.csv', 'rb'))),

    # URL route for saving a location
    path('test/', views.test, name='test'),
]
