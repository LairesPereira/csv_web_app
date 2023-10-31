from django.http import JsonResponse
from django.shortcuts import render
from .form import UploadFileForm
from .handdle_upload import handle_uploaded_file, read_strict

def name_to_filter(request):
        filtered_table = read_strict(request.GET.get('description_filter'))
        if filtered_table == 'empty':
              return JsonResponse({ 'filtered_table': 'Nenhuma transação encontrada'})
        return JsonResponse({'filtered_table': filtered_table,})

def home(request):
    if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            main_table = handle_uploaded_file(request.FILES)
            table_title = 'Todas as Transações'
            return render(request, 'pages/home.html', { 'resultado': main_table, 'table_title': table_title })
    else:
         form = UploadFileForm()
    return render(request, 'pages/home.html', {'form': form})
