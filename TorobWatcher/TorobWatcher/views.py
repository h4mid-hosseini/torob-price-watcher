from django.shortcuts import render



def home(request):
    return render(request, 'index.html')




def about(request):
    return render(request, 'index.html')




def contact(request):
    return render(request, 'index.html')
