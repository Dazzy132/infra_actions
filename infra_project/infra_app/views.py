from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')

def test_page(request):
    return HttpResponse('На боевом проекте изменения прошли')