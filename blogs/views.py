from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the blog index. Sorry, this view is not implemented since it isn't part of requirement.")

