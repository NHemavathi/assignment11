from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'registration/form.html', {'form': form})

def user_list_view(request):
    users = User.objects.all()
    return render(request, 'registration/user_list.html', {'users': users})
