from django.shortcuts import render, HttpResponse


def homepage(request):
    return HttpResponse("<h1>Ciao a tutti! Benvenuti nella homepage!</h1>")


# L2
def menu(request):
    return HttpResponse("<ol><li>Prima opzione</li><li>Seconda opzione</li><li>Terza opzione</li></ol>")


def chisiamo(request):
    return render(request, "chisiamo.html")


def variabili(request):
    context = {'var1': '10', 'var2': 'ciao', 'var3': '123 hello world'}
    return render(request, "variabili.html", context)


def index(request):
    return render(request, "index.html")
