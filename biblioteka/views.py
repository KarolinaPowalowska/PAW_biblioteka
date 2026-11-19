from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<h1>Biblioteka</h1>"
        "<p>Aplikacja Django działa poprawnie.</p>"
    )


def book_list(request):
    return HttpResponse("<h1>Lista książek</h1>")