
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login




def home(request):
    return render(request, 'index.html')




def about(request):
    return render(request, 'index.html')




def contact(request):
    return render(request, 'index.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page or another view after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
