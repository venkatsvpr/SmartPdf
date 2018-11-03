from django.shortcuts import render,redirect
from .forms import FileFormset
from .models import File

# Create your views here.

def index(request):
    template_name = 'index.html'
    heading_message = 'PDF Merger'
    if request.method == 'GET':
        formset = FileFormset(request.GET or None)
    elif request.method == 'POST':
        formset = FileFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # save file instance
                if name:
                    File(name=name).save()
            # once all files are saved, redirect to file list view
            return redirect('file_list')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })