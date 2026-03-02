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
            
            # 1. Cabeçalho
            conteudo = [
                f"Anamnese {data.get('hospital_name', 'Hospital')} - Dia {data.get('data_atendimento', '')}",
                f"Alunos: {data.get('aluno_names', '')}\n",
                
                # 2. Identificação (Formato Narrativo conforme PDF)
                "I – Identificação: " + ", ".join(filter(None, [
                    data.get('nome', ''),
                    f"sexo {data.get('sexo_biologico', '')}" if data.get('sexo_biologico') else None,
                    data.get('idade', ''),
                    data.get('raca_cor', ''),
                    data.get('estado_civil', ''),
                    data.get('religiao', ''),
                    data.get('escolaridade', ''),
                    f"aposentada há {data.get('tempo_aposentadoria', '')}" if data.get('tempo_aposentadoria') else None,
                    f"Natural de {data.get('naturalidade', '')}" if data.get('naturalidade') else None,
                    f"residente em {data.get('residencia_atual', '')}" if data.get('residencia_atual') else None,
                    f"desde os {data.get('tempo_residencia', '')}" if data.get('tempo_residencia') else None,
                ])) + ".\n",

                "II – Queixa Principal e sua duração (QD)",
                f"“{data.get('queixa_principal', '')}”\n",

                "III – História Pregressa da Moléstia Atual (HPMA)",
                f"{data.get('hpma', '')}\n",

                "IV – Interrogatório sobre Sintomas dos Demais Aparelhos (ISDA)",
                f"Sintomas Gerais: {data.get('isda_gerais', '')}",
                f"Pelos e fâneros: {data.get('isda_pele', '')}",
                f"Cabeça: {data.get('isda_cabeca', '')}",
                f"Olhos: {data.get('isda_olhos', '')}",
                f"Nariz: {data.get('isda_nariz', '')}",
                f"Ouvidos: {data.get('isda_ouvidos', '')}",
                f"Boca: {data.get('isda_boca', '')}",
                f"Garganta: {data.get('isda_garganta', '')}",
                f"Pescoço: {data.get('isda_pescoco', '')}",
                f"Tórax e Aparelhos Cardiorrespiratórios: {data.get('isda_torax', '')}",
                f"Abdome e Aparelho Digestório: {data.get('isda_abdome', '')}",
                f"Aparelho Gênito-Urinário: {data.get('isda_genito_urinario', '')}",
                f"Mamas: {data.get('isda_mamas', '')}",
                f"Sistema Neurológico: {data.get('isda_neurologico', '')}",
                f"Saúde Mental: {data.get('isda_saude_mental', '')}",
                f"Aparelho locomotor: {data.get('isda_locomotor', '')}\n",

                "V – Antecedentes",
                f"Antecedentes pessoais: {data.get('antecedentes_morbidos', '')}",
                f"Hábitos de vida: {data.get('habitos_vida', '')}",
                f"Condições de vida: {data.get('condicoes_vida', '')}",
                f"Antecedentes familiares: {data.get('antecedentes_familiares', '')}\n",

                "VII – Exame Físico Geral",
                f"Avaliação do estado geral: {data.get('ef_estado_geral', '')}",
                "Dados vitais:",
                f"- PA: {data.get('ef_pa', '')}",
                f"- FC: {data.get('ef_fc', '')}",
                f"- T: {data.get('ef_t', '')}",
                f"- FR: {data.get('ef_fr', '')}",
                "Dados antropométricos:",
                f"- Peso: {data.get('ef_peso', '')}",
                f"- Altura: {data.get('ef_altura', '')}",
                f"- IMC: {data.get('ef_imc', '')}",
                f"Avaliação do nível de consciência: {data.get('ef_consciencia', '')}",
                f"Avaliação do estado de hidratação: {data.get('ef_hidratacao', '')}",
                f"Avaliação do estado de nutrição: {data.get('ef_nutricao', '')}",
                f"Mucosas: {data.get('ef_mucosas', '')}",
                f"Fácies: {data.get('ef_facies', '')}",
                f"Atitude: {data.get('ef_atitude', '')}",
                "Anexos:",
                f"- Pelos: {data.get('ef_anexos_pelos', '')}",
                f"- Unhas: {data.get('ef_anexos_unhas', '')}",
                f"Pele: {data.get('ef_pele', '')}",
                f"Linfonodos: {data.get('ef_linfonodos', '')}\n",

                "Exame físico do aparelho respiratório:",
                "Inspeção:",
                f"-Estática: {data.get('ef_resp_inspecao_estatica', '')}",
                f"-Dinâmica: {data.get('ef_resp_inspecao_dinamica', '')}",
                f"Percussão: {data.get('ef_resp_percussao', '')}",
                f"Palpação: {data.get('ef_resp_palpacao', '')}",
                f"Ausculta: {data.get('ef_resp_ausculta', '')}\n",

                "Exame físico do aparelho circulatório:",
                f"Inspeção: {data.get('ef_circ_inspecao', '')}",
                f"Palpação: {data.get('ef_circ_palpacao', '')}",
                f"Ausculta: {data.get('ef_circ_ausculta', '')}",
                f"Artérias: {data.get('ef_circ_arterias', '')}",
                f"Pulsos: {data.get('ef_circ_pulsos', '')}\n",

                "VIII. CONCLUSÕES E PLANEJAMENTO",
                "------------------------------",
                f"Hipóteses Diagnósticas: {data.get('hipoteses', '')}",
                f"Exames Complementares: {data.get('exames', '')}",
                f"Plano Terapêutico: {data.get('plano_terapeutico', '')}",
                f"Prognóstico: {data.get('prognostico', '')}"
            ]

            full_text = "\n".join(conteudo)

            # Preparar a resposta como um arquivo para download
            response = HttpResponse(full_text, content_type='text/plain; charset=utf-8')
            
            # Formatar o nome do arquivo usando o nome do paciente e a data
            nome_arq = data.get('nome', 'Paciente').strip().replace(" ", "_").replace(",", "")
            if not nome_arq:
                nome_arq = "Paciente_Anonimo"
            data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
            filename = f"Anamnese_{nome_arq}_{data_atual}.txt"

            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    
    # Se não for POST ou form inválido, redireciona pro home
    return render(request, 'generator/home.html', {'form': AnamneseForm()})
