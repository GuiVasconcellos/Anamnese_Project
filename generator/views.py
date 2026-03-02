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
                f"Anamnese {data.get('hospital_name', 'Hospital')} - Dia {data.get('data_atendimento', '')}" if data.get('hospital_name') or data.get('data_atendimento') else None,
                f"Alunos: {data.get('aluno_names', '')}\n" if data.get('aluno_names') else None,
                
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
                f"“{data.get('queixa_principal', '')}”\n" if data.get('queixa_principal') else None,

                "III – História Pregressa da Moléstia Atual (HPMA)",
                f"{data.get('hpma', '')}\n" if data.get('hpma') else None,

                "IV – Interrogatório sobre Sintomas dos Demais Aparelhos (ISDA)",
                f"Sintomas Gerais: {data.get('isda_gerais', '')}" if data.get('isda_gerais') else None,
                f"Pelos e fâneros: {data.get('isda_pele', '')}" if data.get('isda_pele') else None,
                f"Cabeça: {data.get('isda_cabeca', '')}" if data.get('isda_cabeca') else None,
                f"Olhos: {data.get('isda_olhos', '')}" if data.get('isda_olhos') else None,
                f"Nariz: {data.get('isda_nariz', '')}" if data.get('isda_nariz') else None,
                f"Ouvidos: {data.get('isda_ouvidos', '')}" if data.get('isda_ouvidos') else None,
                f"Boca: {data.get('isda_boca', '')}" if data.get('isda_boca') else None,
                f"Garganta: {data.get('isda_garganta', '')}" if data.get('isda_garganta') else None,
                f"Pescoço: {data.get('isda_pescoco', '')}" if data.get('isda_pescoco') else None,
                f"Tórax e Aparelhos Cardiorrespiratórios: {data.get('isda_torax', '')}" if data.get('isda_torax') else None,
                f"Abdome e Aparelho Digestório: {data.get('isda_abdome', '')}" if data.get('isda_abdome') else None,
                f"Aparelho Gênito-Urinário: {data.get('isda_genito_urinario', '')}" if data.get('isda_genito_urinario') else None,
                f"Mamas: {data.get('isda_mamas', '')}" if data.get('isda_mamas') else None,
                f"Sistema Neurológico: {data.get('isda_neurologico', '')}" if data.get('isda_neurologico') else None,
                f"Saúde Mental: {data.get('isda_saude_mental', '')}" if data.get('isda_saude_mental') else None,
                f"Aparelho locomotor: {data.get('isda_locomotor', '')}\n" if data.get('isda_locomotor') else None,

                "V – Antecedentes",
                f"Antecedentes pessoais: {data.get('antecedentes_morbidos', '')}" if data.get('antecedentes_morbidos') else None,
                f"Hábitos de vida: {data.get('habitos_vida', '')}" if data.get('habitos_vida') else None,
                f"Condições de vida: {data.get('condicoes_vida', '')}" if data.get('condicoes_vida') else None,
                f"Antecedentes familiares: {data.get('antecedentes_familiares', '')}\n" if data.get('antecedentes_familiares') else None,

                "VII – Exame Físico Geral",
                f"Avaliação do estado geral: {data.get('ef_estado_geral', '')}" if data.get('ef_estado_geral') else None,
                "Dados vitais:" if any([data.get('ef_pa'), data.get('ef_fc'), data.get('ef_t'), data.get('ef_fr')]) else None,
                f"- PA: {data.get('ef_pa', '')}" if data.get('ef_pa') else None,
                f"- FC: {data.get('ef_fc', '')}" if data.get('ef_fc') else None,
                f"- T: {data.get('ef_t', '')}" if data.get('ef_t') else None,
                f"- FR: {data.get('ef_fr', '')}" if data.get('ef_fr') else None,
                "Dados antropométricos:" if any([data.get('ef_peso'), data.get('ef_altura'), data.get('ef_imc')]) else None,
                f"- Peso: {data.get('ef_peso', '')}" if data.get('ef_peso') else None,
                f"- Altura: {data.get('ef_altura', '')}" if data.get('ef_altura') else None,
                f"- IMC: {data.get('ef_imc', '')}" if data.get('ef_imc') else None,
                f"Avaliação do nível de consciência: {data.get('ef_consciencia', '')}" if data.get('ef_consciencia') else None,
                f"Avaliação do estado de hidratação: {data.get('ef_hidratacao', '')}" if data.get('ef_hidratacao') else None,
                f"Avaliação do estado de nutrição: {data.get('ef_nutricao', '')}" if data.get('ef_nutricao') else None,
                f"Mucosas: {data.get('ef_mucosas', '')}" if data.get('ef_mucosas') else None,
                f"Fácies: {data.get('ef_facies', '')}" if data.get('ef_facies') else None,
                f"Atitude: {data.get('ef_atitude', '')}" if data.get('ef_atitude') else None,
                "Anexos:" if any([data.get('ef_anexos_pelos'), data.get('ef_anexos_unhas')]) else None,
                f"- Pelos: {data.get('ef_anexos_pelos', '')}" if data.get('ef_anexos_pelos') else None,
                f"- Unhas: {data.get('ef_anexos_unhas', '')}" if data.get('ef_anexos_unhas') else None,
                f"Pele: {data.get('ef_pele', '')}" if data.get('ef_pele') else None,
                f"Linfonodos: {data.get('ef_linfonodos', '')}\n" if data.get('ef_linfonodos') else None,

                "Exame físico do aparelho respiratório:" if any([data.get('ef_resp_inspecao_estatica'), data.get('ef_resp_inspecao_dinamica'), data.get('ef_resp_percussao'), data.get('ef_resp_palpacao'), data.get('ef_resp_ausculta')]) else None,
                "Inspeção:" if any([data.get('ef_resp_inspecao_estatica'), data.get('ef_resp_inspecao_dinamica')]) else None,
                f"-Estática: {data.get('ef_resp_inspecao_estatica', '')}" if data.get('ef_resp_inspecao_estatica') else None,
                f"-Dinâmica: {data.get('ef_resp_inspecao_dinamica', '')}" if data.get('ef_resp_inspecao_dinamica') else None,
                f"Percussão: {data.get('ef_resp_percussao', '')}" if data.get('ef_resp_percussao') else None,
                f"Palpação: {data.get('ef_resp_palpacao', '')}" if data.get('ef_resp_palpacao') else None,
                f"Ausculta: {data.get('ef_resp_ausculta', '')}\n" if data.get('ef_resp_ausculta') else None,

                "Exame físico do aparelho circulatório:" if any([data.get('ef_circ_inspecao'), data.get('ef_circ_palpacao'), data.get('ef_circ_ausculta'), data.get('ef_circ_arterias'), data.get('ef_circ_pulsos')]) else None,
                f"Inspeção: {data.get('ef_circ_inspecao', '')}" if data.get('ef_circ_inspecao') else None,
                f"Palpação: {data.get('ef_circ_palpacao', '')}" if data.get('ef_circ_palpacao') else None,
                f"Ausculta: {data.get('ef_circ_ausculta', '')}" if data.get('ef_circ_ausculta') else None,
                f"Artérias: {data.get('ef_circ_arterias', '')}" if data.get('ef_circ_arterias') else None,
                f"Pulsos: {data.get('ef_circ_pulsos', '')}\n" if data.get('ef_circ_pulsos') else None,

                "VIII. CONCLUSÕES E PLANEJAMENTO",
                "------------------------------",
                f"Hipóteses Diagnósticas: {data.get('hipoteses', '')}" if data.get('hipoteses') else None,
                f"Exames Complementares: {data.get('exames', '')}" if data.get('exames') else None,
                f"Plano Terapêutico: {data.get('plano_terapeutico', '')}" if data.get('plano_terapeutico') else None,
                f"Prognóstico: {data.get('prognostico', '')}" if data.get('prognostico') else None
            ]

            full_text = "\n".join(filter(None, conteudo))

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
