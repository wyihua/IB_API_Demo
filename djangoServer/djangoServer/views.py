from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, render



# Define an hashable class as context for render method
# class Hero:
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    # def __eq__(self, obj):
    #     return self.name == obj.name

    # def __hash__(self):
    #     return hash((self.name))


def index(request):
    # return HttpResponse("demo reply")
    item_list = [4, 5, 7, 8]
    context = {}
    # context[1] = 1

    # hero = Hero('myName', '18')

    return render(request, 'djangoServer/index.html',)


class IndexView(generic.ListView):
    template_name = './index.html'