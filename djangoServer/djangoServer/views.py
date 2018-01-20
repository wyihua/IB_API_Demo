from django.http import HttpResponse
from django.views import generic


def index(request):
    return HttpResponse("demo reply")


class IndexView(generic.ListView):
    template_name = 'polls/results.html'