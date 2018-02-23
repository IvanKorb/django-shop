from django.shortcuts import render
from .forms import ClientForm

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
