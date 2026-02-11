from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *

def LPU(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("wowowowow")

def save_data(request):
    print(request.POST)
    title = request.POST.get("title", "")
    description = request.POST.get("description", "")
    if not title or not description:
            messages.error(request, "Fill all details")
            return redirect("/")
    note = Note(title=title,description=description)
    note.save()
    messages.success(request,"Details Saved")
    return redirect("/")
    # if request.method == "POST":
    #     title = request.POST.get("title", "")
    #     description = request.POST.get("description", "")

    #     if not title or not description:
    #         messages.error(request, "Fill all details")
    #         return redirect("/")

    #     Note.objects.create(
    #         title=title,
    #         description=description
    #     )

    #     messages.success(request, "Note added successfully")
    #     return redirect("/")