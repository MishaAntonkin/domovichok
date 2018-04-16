import requests
import json

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
        print(request.body)
        print(json.loads(request.body))
        print(request.POST.dict())
        houses = form.data.get('houses')
        criterias = form.data.get('cri')
        r = requests.post('http://127.0.0.1:5000/', timeout=10, data=request.body)
        print(r.json())
        if form.is_valid():
            r = requests.post('http://127.0.0.1:5000/', data=form.cleaned_data)
            print(r.text)
            print(form.cleaned_data)
        return redirect(reverse('selectplace:filldata'))