from django.shortcuts import render

# responsável pela página principal da aplicação
def index(request):
    return render(request, 'index.html') 