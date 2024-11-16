from django.shortcuts import render
from . forms import TravelForm

from .models import Travel

# Create your views here. 
def travel(request):
 form = TravelForm()
 if request.method == 'POST':
  form = TravelForm(request.POST)
  if form.is_valid():
   name = form.cleaned_data['name']
   email = form.cleaned_data['email']   
   travelfrom = form.cleaned_data['travelFrom']
   travelto = form.cleaned_data['travelTo']
   traveldate = form.cleaned_data['travelDate']
   Travel.objects.create(name=name, email=email, travelfrom=travelfrom, travelto=travelto, traveldate=traveldate)   
   return render(request, 'travelformapp/success.html', {'name': name})
 return render(request, 'travelformapp/travel.html', {'form': form})
