from django.shortcuts import render
from .models import ProductMini
from .models import HeaderNav
from .models import HeaderInfo
from .models import IMG
from .models import Section

def index(request):
    sections = Section.objects.all()
    imgs = IMG.objects.all()
    infos = HeaderInfo.objects.all()
    headers = HeaderNav.objects.all()
    mini = ProductMini.objects.all()
    return render(request, 'index.html', { 'mini': mini, 'headers' : headers, 'infos': infos, 'imgs' : imgs,'sections': sections })
