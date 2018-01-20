from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, render


def index(request):
    # return HttpResponse("demo reply")
    return render(request, 'djangoServer/index.html',)


class IndexView(generic.ListView):
    template_name = './index.html'