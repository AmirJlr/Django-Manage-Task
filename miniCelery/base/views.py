from django.shortcuts import render
from .forms import InviteForm
from .tasks import send_invite_email
# Create your views here.

def form_view(request):
    
    if request.method == 'GET':
        form = InviteForm()

    elif request.method == 'POST':
        form = InviteForm(request.POST)

        if form.is_valid():
            send_invite_email.delay()
            return render(request, 'base/success.html')

        else:
            return render(request, 'base/form.html', {'form':form})


    
