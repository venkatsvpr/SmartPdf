from django.shortcuts import render
from .forms import FileFormset
from .models import File
import sys

#sys.path.append(0,")
# Create your views here.

def index(request):
    template_name = 'index.html'
    heading_message = 'PDF Merger'
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
                # save file instance
                if name and pagenos:
                    File(name=name,pages = pagenos).save()
                
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })