from django.shortcuts import render
from .forms import ClientForm
from products.models import *


# Create your views here.
def landing(request):
    name = "Ivan Kor"
    current_day = "20.02.2018"
    form = ClientForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        # print(form.cleaned_data)
        # data = form.cleaned_data
        # print(data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_recommend = products_images.filter(product__category_id=1)
    products_images_classic = products_images.filter(product__category_id=2)
    return render(request, 'landing/home.html', locals())
