from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def ops(request):
    list_of_hotels = {'htl1': {'name': 'Cumberland Hotel', 'address': '01 Marble Arch', 'city': 'London'},
                      'htl2': {'name': 'Hyatt Churchil', 'address': '47 Portman Square', 'city': 'London'},
                      'htl3': {'name': 'Lindner Grand Hotel', 'address': '5 Honwegg Road', 'city': 'Interlaken'},
                      'htl4': {'name': 'Pullman Hotel Paris La Defence', 'address': 'La Defence', 'city': 'Paris'},
                      'htl5': {'name': 'Grand National Hotel Lucerne', 'address': 'High Street', 'city': 'Lucerne'},
                      'htl6': {'name': 'Movenpick Hotel Zurich', 'address': 'Railway Road', 'city': 'Zurich'}
                      }
    accommodation = {'hotels': list_of_hotels}
    return render(request, 'operations/ops.html', context=accommodation)