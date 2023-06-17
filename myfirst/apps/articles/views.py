from django.http import HttpResponse

def index(request):
    return HttpResponse("Это мой первый сайт!")