from django.shortcuts import render
from django.http import HttpResponse

from .models import Apiary, Hive, Colony
# Create your views here.


def index(request):
    apiaries = Apiary.objects.order_by('start_date', 'name')
    context = {'apiaries': apiaries, }
    return render(request, 'colony/index.html', context)

def apiary_detail(request, apiary_id):
    apiary = Apiary.objects.get(pk=apiary_id)
    hives = Hive.objects.filter(apiary_id=apiary_id)
    context = {'apiary': apiary, 'hives': hives, }
    return render(request, 'colony/apiary_detail.html', context)

def hive_detail(request, hive_id):
    hive = Hive.objects.get(pk=hive_id)
    apiary = Apiary.objects.get(pk=hive.apiary_id.id)
    context = {'hive': hive, 'apiary': apiary, 'colonies': None}
    return render(request, 'colony/hive_detail.html', context)

def colony_detail(request, colony_id):
    colony = colony.objects.get(pk=colony_id)
    context = {'colony': colony, }
    return render(request, 'colony/colony_detail.html', context)
    