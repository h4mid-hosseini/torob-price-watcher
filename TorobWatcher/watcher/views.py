from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from . import watcher, models, forms


def home(request):
    return render(request, 'index.html')



def update_product_price(request):
    watcher.release_dogs()

    return HttpResponse('Price Updated')



@login_required
def current_product_under_watch(request):
    products = models.WatchingProducts.objects.filter(user = request.user)

    return render(request, 'watcher/list.html', {'products':products})



@login_required
def edit_under_watch_product(request, pk):
    product = models.WatchingProducts.objects.filter(pk=pk, user=request.user)



@login_required
def delete_under_watch_product(request, pk):
    product = models.WatchingProducts.objects.filter(pk=pk, user=request.user).first()

    if product != None:
        product.delete()
        messages.warning(request, 'The Item Deleted!')
        return redirect('watcher:list')
    
    messages.error(request, 'Item Does Not Exist')
    return redirect('watcher:list')



@login_required
def create_watching_product(request):
    if request.method == 'POST':
        data = request.POST
        form = forms.WatchingProductsForm(data)
        if form.is_valid():
            watching_form = form.save(commit=False)
            watching_form.user = request.user
            watching_form.save()
            return redirect('watcher:list')
    else:
        form = forms.WatchingProductsForm()
    return render(request, 'watcher/create.html', {'form': form})