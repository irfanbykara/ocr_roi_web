
# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

def home(request):

    if request.method == 'POST':
        rectangles = request.POST.getlist('rectangles[]')  # Assuming rectangles is an array of objects
        # Process the rectangles data here

        # Return a response, for example, a JSON response
        print(rectangles)
        return JsonResponse({'success': True})
    return render( request, 'main/index.html', )

def convert_to_text(request):
    if request.method == 'POST':
        # rectangles_json = request.POST.get('rectangles')
        # print(rectangles_json)

        try:
            rectangles_json = request.POST.get('rectangles')
            rectangles = json.loads(rectangles_json)  # Parse JSON data
            for rect in rectangles:
                # Process the coordinates as needed
                print(f"StartX: {rect['startX']}, StartY: {rect['startY']}, EndX: {rect['endX']}, EndY: {rect['endY']}")
            return JsonResponse({'success': True})
        except json.JSONDecodeError as e:
            print('?' * 50)
            print(e)
            print('?' * 50)
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
