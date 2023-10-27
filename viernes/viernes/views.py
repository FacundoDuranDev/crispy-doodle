from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request): #=> nombre del protocolo http que se va a usar
        with open("./viernes/templates/home.html") as archivo:
            contenido = archivo.read()
        return HttpResponse(contenido)