from django.shortcuts import render
from datetime import datetime
# Create your views here.


def prd(request):
    add = ['Cumberland', 'Hyatt Churchil', 'Hilton London on Park Lane', 'Amba Marble Arch',
                      'Corus Hyde Park', 'Bayswater Hotel', 'Royal National London']
    htl = 'Add Hotel/Service Apartment/Lodge/B&B'
    att = 'Add Attraction'
    tic = 'Add Tickets'
    trf = 'Add Transfers'
    d = datetime.now()
    prd_detail = {'ht':htl, 'at':att, 'ti': tic, 'tr': trf, 'dt': d, 'ads':add}
    return render(request, 'products/prd.html', context=prd_detail)


def hotel(request):
    return render(request, 'products/hotel.html')
