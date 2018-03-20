import requests

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import PlaceFilterForm
# Create your views here.


class FillData(View):

    def get(self, request):
        form = PlaceFilterForm()
        return render(request, 'selectplace/filldata.html', locals())

    def post(self, request):
        form = PlaceFilterForm(request.POST)
        if form.is_valid():
            r = requests.post('http://127.0.0.1:5000/', data=form.cleaned_data)
            print(r.text)
            print(form.cleaned_data)
        return redirect(reverse('selectplace:filldata'))