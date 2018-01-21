from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

import _thread

from .models import Ticket
from ibpy import ib_api_demo


def index(request):
    # getMktdata()

    if(request.GET.get('addData')):
        t = Ticket()
        t.save()
        _thread.start_new_thread(getMktdata, ())

    
    if(request.GET.get('clearData')):
        # print("get clearData request")
        Ticket.objects.all().delete()

    context = {'ticket_list': Ticket.objects}
    return render(request, 'ibhandler/index.html', context)



# Call IB API to get market data
def getMktdata():
    # print("you will get data!")

    ticket_data = ib_api_demo.getMktData()
    print(ticket_data)

