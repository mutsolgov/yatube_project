from django.shortcuts import HttpResponse #render



def index(request):
    return HttpResponse('Это главная страница.')


def group_posts(request):
    return HttpResponse('Здесь может быть список постов.')


# # В урл мы ждем парметр, и нужно его прередать в функцию для использования
# def ice_cream_detail(request, pk):
#     return HttpResponse(f'Мороженое номер {pk}')

# Create your views here.
