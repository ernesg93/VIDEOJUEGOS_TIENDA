from django.shortcuts import render

# Vista de la pagina principal
def index(request):
    #render toma el request y el archivo HTML que queremos mostrar
    return render(request, 'home/index.html')

# Vista de la pagina de contacto
def contacto(request):
    return render(request, 'home/contacto.html')

