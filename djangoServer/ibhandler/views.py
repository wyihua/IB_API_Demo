from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import Ticket


# def index(request):
#     return HttpResponse("Hello, world. You're at the IB handler index.")

# class ResultsView(generic.ListView):
#     template_name = 'ibhandler/index.html'
#     model = Ticket

#     def get_queryset(self):
#         return Ticket.objects

def index(request):
    return render(request, 'ibhandler/index.html',)

