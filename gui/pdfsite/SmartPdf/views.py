from django.shortcuts import render,redirect
from .forms import FileFormset
from .models import File
from django.contrib import messages
import sys


sys.path.insert(0,'D:\Projects\Django Projects\SmartPdf\\backend')

from Main import *
# Create your views here.

def index(request):
    template_name = 'form.html'
    heading_message = 'PDF Merger'
    inputpaths = []
    pagelists = []
    if request.method == 'GET':
        formset = FileFormset(request.GET or None)
    elif request.method == 'POST':
        for x in File.objects.all():
            x.delete()

        formset = FileFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                pagenos = form.cleaned_data.get('pages')
                inputpaths.append(name)
                maxPageCount = getMaxPageCount(name)
                pagelists.append(expandPages(pagenos,maxPageCount))
                # save file instance
                if name and pagenos:
                    File(name=name,pages = pagenos).save()
            MergePdf(inputpaths,pagelists,["hello"],r"D:\Downloads\merged.pdf")
            return redirect('complete')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })
    
def complete(request):
    template_name = 'alert.html'
    return render(request,template_name)
