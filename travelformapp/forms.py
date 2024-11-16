from django import forms

class TravelForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    travelFrom = forms.CharField(max_length=100, label='Travel From')
    travelTo = forms.CharField(max_length=100, label='Travel To')
    travelDate = forms.DateField(label='Travel Date')