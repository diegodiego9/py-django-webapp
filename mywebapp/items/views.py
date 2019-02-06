from django.http import HttpResponse


# simplest view possible
def home(request):
    return HttpResponse("Hello, world. You're at the Items-app homepage.")

