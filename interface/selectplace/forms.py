from django import forms


class PlaceFilterForm(forms.Form):
    currency_choices = [('UAH', 'грн'), ('USD', '$'), ('EUR', '€')]
    district = forms.CharField(label="Select district")
    street = forms.CharField(label='Select street name')
    currency = forms.ChoiceField(choices=currency_choices)
    min_price = forms.IntegerField(label="Select min price")
    max_price = forms.IntegerField(label='Select max price')
