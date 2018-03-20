from django import forms


class PlaceFilterForm(forms.Form):
    district = forms.CharField(label="Select district")
    price = forms.IntegerField(label="Select price")
