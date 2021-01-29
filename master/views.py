from django.shortcuts import render
from service.models import Service
# Create your views here.

def index_func(request):

    #получаем список статей
    service_list = Service.objects.all();

    context = {
        'service_list': service_list
    }

    return render(request, 'master/index.html', context)

def contacts_func(req):
    return render(req, 'master/contacts.html')

def about_us_func(req):
    return render(req, 'master/about_us.html')

def faq_func(req):
    return render(req, 'master/faq.html')