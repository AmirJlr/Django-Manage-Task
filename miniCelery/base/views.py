from django.shortcuts import render
from .forms import InviteForm
# Create your views here.

def form_view(request):
    
    if request.method == 'GET':
        form = InviteForm()

    elif request.method == 'POST':
        form = request.POST


    return render(request, 'base/form.html', {'form':form})
