from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

import _thread

from .models import Ticket
from ibpy import ib_api_demo


def index(request):
    # getMktdata()

    if(request.GET.get('addData')):
        _thread.start_new_thread(getMktdata, ())
    
    if (request.GET.get('buyTicket')):
        _thread.start_new_thread(ib_api_demo.buyTicket, ())

    
    if(request.GET.get('clearData')):
        # print("get clearData request")
        Ticket.objects.all().delete()
    


    context = {'ticket_list': Ticket.objects}
    return render(request, 'ibhandler/index.html', context)



# Call IB API to get market data
def getMktdata():
    # print("you will get data!")

    ticket_data = ib_api_demo.getMktData()
    # print(ticket_data)
    print('field is :', ticket_data['field'][0])
    print('price is :', ticket_data['price'][0])

    t = Ticket()
    for id in range(len(ticket_data['ticketId'])):
        curId = id
        if (ticket_data['field'][curId] == 1):
            t.bcurId_price = ticket_data['price'][curId]
        if (ticket_data['field'][curId] == 2):
            t.ask_price = ticket_data['price'][curId]
        if (ticket_data['field'][curId] == 9):
            t.close_price = ticket_data['price'][curId]
    print(t)
    t.save()
