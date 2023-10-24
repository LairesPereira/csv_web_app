from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .form import UploadFileForm
from .handdle_upload import handle_uploaded_file
# Create your views here.

def teste(request):
      print('feito')
      return HttpResponse('Olá')

def home(request):
    if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            result = handle_uploaded_file(request.FILES)
            full_table = False
            return render(request, 'pages/home.html', { 'resultado': result, 'full_table': full_table })
    else:
         form = UploadFileForm()
    return render(request, 'pages/home.html', {'form': form})
