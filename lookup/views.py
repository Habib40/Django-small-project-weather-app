import requests
import json
from django.shortcuts import render

def index(request):
    zipcode = None
    api = None
    error_message = None

    if request.method == 'POST':
        zipcode = request.POST.get('zipcode')

        if zipcode:
            # Fetch data from the API
            api_request = requests.get(f'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=5&API_KEY=B999E89C-FAE7-4CDB-8CD4-923A26D9263B')
            try:
                api = json.loads(api_request.content)
                if 'WebServiceError' in api:
                    error_message = api['WebServiceError'][0]['Message']
                print(api)  # Debugging line to see the API response
            except json.JSONDecodeError:
                error_message = "Error fetching data"

    return render(request, 'home.html', {'api': api, 'zipcode': zipcode, 'error_message': error_message})