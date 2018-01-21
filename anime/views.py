from django.http import HttpResponse
from django.template import loader

from .models import Anime


def index(request):
    anime_list = Anime.objects.all()
    template = loader.get_template('anime_list.html')
    context = {
        'anime_list': anime_list,
    }
    return HttpResponse(template.render(context, request))
