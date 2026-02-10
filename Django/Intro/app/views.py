from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

def LPU(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("wowowowow")

def save_data(req):
    print(req.POST)
    title = req.POST.get("title", "")
    description = req.POST.get("description", "")

    if not title or not description:
            messages.error(req, "Fill all details")
            return redirect("/")

        
    return HttpResponse(f"Details saved")