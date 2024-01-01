from django.shortcuts import render
from .models import Notes
# Create your views here.

## chapter 4
def list(request):
    all_notes = Notes.objects.all()  ## importing the first model from models.py
    return render(request, 'notes/notes_list.html', {'notes': all_notes}) #we should have notes_html.html
