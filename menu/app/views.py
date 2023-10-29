from django.shortcuts import render
from app.models import Elements

def index(request):
    menu = Elements.objects.all()
    context = {'menu': menu}
    return render(request, 'app/index.html', context)
