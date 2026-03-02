from django.shortcuts import render
from django.http import HttpResponse
from .forms import AnamneseForm
import datetime

def home_view(request):
    form = AnamneseForm()
    return render(request, 'generator/home.html', {'form': form})

def generate_txt_view(request):
    if request.method == 'POST':
        form = AnamneseForm(request.POST)
        if form.is_valid():
            # Construir o texto do TXT baseado no form preenchido
            data = form.cleaned_data
            
            conteudo = [
                "=================================================",
                "         ROTEIRO DE HISTÓRIA CLÍNICA           ",
                "=================================================\n",
                
                "I. IDENTIFICAÇÃO",
                "-----------------",
                f"Nome / Nome social: {data.get('nome', '')}",
                f"Idade / Data de nascimento: {data.get('idade', '')}",
                f"Sexo biológico: {data.get('sexo_biologico', '')}",
                f"Identidade de gênero: {data.get('identidade_genero', '')}",
                f"Raça / Cor / Etnia: {data.get('raca_cor', '')}",
                f"Naturalidade: {data.get('naturalidade', '')}",
                f"Nacionalidade: {data.get('nacionalidade', '')}",
                f"Procedência Próxima: {data.get('procedencia_proxima', '')}",
                f"Procedência Remota: {data.get('procedencia_remota', '')}",
                f"Religião: {data.get('religiao', '')}",
                f"Profissão: {data.get('profissao', '')}",
                f"Estado Civil: {data.get('estado_civil', '')}",
                f"Escolaridade: {data.get('escolaridade', '')}",
                f"Profissional responsável: {data.get('face_atendimento', '')}\n",

                "II. QUEIXA PRINCIPAL E DURAÇÃO (QD)",
                "-----------------------------------",
                f"{data.get('queixa_principal', '')}\n",

                "III. HISTÓRIA PREGRESSA DA MOLÉSTIA ATUAL (HPMA)",
                "------------------------------------------------",
                f"{data.get('hpma', '')}\n",

                "IV. INTERROGATÓRIO SOBRE OS SINTOMAS DOS DEMAIS APARELHOS (ISDA)",
                "----------------------------------------------------------------",
                f"Sintomas gerais: \n{data.get('isda_gerais', '')}\n",
                f"Pele e fâneros: \n{data.get('isda_pele', '')}\n",
                f"Cabeça: \n{data.get('isda_cabeca', '')}\n",
                f"Pescoço: \n{data.get('isda_pescoco', '')}\n",
                f"Tórax e Aparelhos Cardio e Respiratório: \n{data.get('isda_torax', '')}\n",
                f"Abdome e Aparelho Digestório: \n{data.get('isda_abdome', '')}\n",
                f"Aparelho Gênito-Urinário: \n{data.get('isda_genito_urinario', '')}\n",
                f"Sistema Nervoso: \n{data.get('isda_neurologico', '')}\n",
                f"Saúde mental / psiquismo: \n{data.get('isda_saude_mental', '')}\n",
                f"Sistema Osteo-Articular e Muscular: \n{data.get('isda_locomotor', '')}\n",
                f"Sistema Endócrino: \n{data.get('isda_endocrino', '')}\n",
                f"Sistemas Imunológico e Linfohematopoético: \n{data.get('isda_imunologico', '')}\n",

                "V. ANTECEDENTES",
                "---------------",
                f"Antecedentes mórbidos: \n{data.get('antecedentes_morbidos', '')}\n",
                f"Hábitos de vida: \n{data.get('habitos_vida', '')}\n",
                f"Condições de vida: \n{data.get('condicoes_vida', '')}\n",
                f"Antecedentes epidemiológicos: \n{data.get('epidemiologia', '')}\n",
                f"Vacinação: \n{data.get('vacinacao', '')}\n",
                f"Medicamentos de uso contínuo: \n{data.get('medicamentos_uso', '')}\n",
                f"Antecedentes Familiares: \n{data.get('antecedentes_familiares', '')}\n",

                "VI. EXAME FÍSICO",
                "----------------",
                f"Exame Físico Geral: \n{data.get('ef_geral', '')}\n",
                f"Cabeça e Pescoço: \n{data.get('ef_cabeca_pescoco', '')}\n",
                f"Exame Físico do Tórax: \n{data.get('ef_torax', '')}\n",
                f"Exame Físico do Abdome: \n{data.get('ef_abdome', '')}\n",
                f"Exame Neurológico: \n{data.get('ef_neurologico', '')}\n",
                f"Aparelho Locomotor: \n{data.get('ef_locomotor', '')}\n",

                "VII. HIPÓTESES DIAGNÓSTICAS",
                "---------------------------",
                f"{data.get('hipoteses', '')}\n",

                "VIII. EXAMES COMPLEMENTARES",
                "---------------------------",
                f"{data.get('exames', '')}\n",
                
                "IX. PLANO TERAPÊUTICO",
                "---------------------",
                f"{data.get('plano_terapeutico', '')}\n",
                
                "X. PROGNÓSTICO",
                "--------------",
                f"{data.get('prognostico', '')}\n"
            ]

            full_text = "\n".join(conteudo)

            # Preparar a resposta como um arquivo para download
            response = HttpResponse(full_text, content_type='text/plain; charset=utf-8')
            
            # Formatar o nome do arquivo usando o nome do paciente e a data
            nome_arq = data.get('nome', 'Paciente').strip().replace(" ", "_")
            if not nome_arq:
                nome_arq = "Paciente_Anonimo"
            data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
            filename = f"Anamnese_{nome_arq}_{data_atual}.txt"

            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    
    # Se não for POST ou form inválido, redireciona pro home
    return render(request, 'generator/home.html', {'form': AnamneseForm()})
