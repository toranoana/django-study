from django.http import HttpResponse
from django.template import loader

from .models import Anime, CV, AnimeCV


def index(request):
    anime_list = Anime.objects.all()
    template = loader.get_template('anime_list.html')
    context = {
        'anime_list': anime_list,
    }
    return HttpResponse(template.render(context, request))


def anime(request, anime_id):
    anime = Anime.objects.get(pk=anime_id)
    # TODO: 外部キー活用してワンライナーで取得
    anime_cvs = AnimeCV.objects.filter(anime_id=anime_id)
    cv_list = CV.objects.filter(id__in=[anime_cv.cv_id for anime_cv in anime_cvs])
    template = loader.get_template('anime.html')
    context = {
        'anime': anime,
        'cv_list': cv_list,
    }
    return HttpResponse(template.render(context, request))
