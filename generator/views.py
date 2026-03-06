from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import AnamneseForm
from xhtml2pdf import pisa
import datetime
import io
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .ai_service import extract_anamnese_data

def home_view(request):
    form = AnamneseForm()
    return render(request, 'generator/home.html', {'form': form})

def generate_pdf_view(request):
    if request.method == 'POST':
        form = AnamneseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            # Renderizar o template HTML para o PDF
            template_path = 'generator/pdf_template.html'
            context = {'data': data}
            
            # Criar um objeto de resposta Django e especificar o content_type como pdf
            response = HttpResponse(content_type='application/pdf')
            
            # Formatar o nome do arquivo usando o nome do paciente e a data
            nome_paciente = data.get('nome', 'Paciente').strip().replace(" ", "_").replace(",", "")
            if not nome_paciente:
                nome_paciente = "Paciente_Anonimo"
            data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
            filename = f"Anamnese_{nome_paciente}_{data_atual}.pdf"
            
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            # Encontrar o template e renderizá-lo
            template = get_template(template_path)
            html = template.render(context)

            # Criar o PDF
            pisa_status = pisa.CreatePDF(
                io.BytesIO(html.encode("utf-8")), 
                dest=response,
                encoding='utf-8'
            )
            
            # Se houver erro, retornar um erro amigável
            if pisa_status.err:
               return HttpResponse('Erro no pisa.CreatePDF <pre>' + html + '</pre>')
            
            return response
    
    # Se o form for inválido ou não for POST
    form = AnamneseForm(request.POST) if request.method == 'POST' else AnamneseForm()
    return render(request, 'generator/home.html', {'form': form})

@csrf_exempt
def api_parse_anamnese(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            text = body.get('text', '')
            if not text:
                return JsonResponse({'error': 'Nenhum texto fornecido'}, status=400)
            
            extracted_data = extract_anamnese_data(text)
            return JsonResponse(extracted_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método não permitido'}, status=405)
