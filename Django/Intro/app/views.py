from django.shortcuts import render
from django.http import HttpResponse

def LPU(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("wowowowow")

def save_data(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        # Process your data here (save to database, etc.)
        # For now, just return a response
        return HttpResponse(f"Data received! Title: {title}, Description: {description}")
    else:
        return HttpResponse("Please submit the form.")