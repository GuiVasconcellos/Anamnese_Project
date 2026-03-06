import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-2.5-flash', generation_config={"response_mime_type": "application/json"})

def extract_anamnese_data(text):
    """
    Usa o Gemini para extrair dados estruturados de um texto de anamnese.
    """
    prompt = f"""
    Você é um assistente médico especializado em transcrição de prontuários.
    Sua tarefa é extrair o máximo de informações do texto fornecido e retornar em formato JSON estritamente seguindo estas chaves (apenas as que encontrar):
    
    Chaves possíveis:
    nome, nome_social, idade, data_nascimento, sexo_biologico, raca_cor, estado_civil, religiao, escolaridade,
    profissao, aposentadoria, naturalidade, nacionalidade, procedencia_prox, procedencia_rem, residencia_atual,
    tempo_residencia, identidade_genero, queixa_principal, hpma, isda_gerais, isda_pele, isda_cabeca, isda_olhos,
    isda_nariz, isda_ouvidos, isda_boca, isda_garganta, isda_pescoco, isda_torax, isda_abdome, isda_urinario,
    isda_repro_fem, isda_repro_masc, isda_mamas, isda_neurologico, isda_saude_mental, isda_locomotor, isda_endocrino,
    isda_imunologico, ant_morbidos, habitos_vida, condicoes_vida, epidemiologia, vacinacao, medicamentos_uso,
    ant_familiares, ef_estado_geral, ef_pa, ef_fc, ef_t, ef_fr, ef_peso, ef_altura, ef_imc, ef_consciencia,
    ef_hidratacao, ef_nutricao, ef_mucosas, ef_facies, ef_atitude, ef_anexos_pelos, ef_anexos_unhas, ef_pele,
    ef_linfonodos, ef_resp_insp_est, ef_resp_insp_din, ef_resp_percussao, ef_resp_palpacao, ef_resp_ausculta,
    ef_circ_inspecao, ef_circ_palpacao, ef_circ_ausculta, ef_circ_arterias, ef_circ_pulsos, ef_cabeca_detalhe,
    ef_pescoco_detalhe, ef_abdome_especial, ef_neuro_detalhe, ef_locomotor_detalhe, hipoteses, exames,
    plano_terapeutico, prognostico.

    REGRAS:
    1. Retorne APENAS o objeto JSON.
    2. Use strings para todos os valores.
    3. Se não encontrar uma informação, NÃO inclua a chave no JSON.
    4. Se o texto mencionar vários sintomas, agrupe-os logicamente na chave correta (ex: dores no peito em 'isda_torax').

    TEXTO DO MÉDICO:
    "{text}"
    """
    
    try:
        response = model.generate_content(prompt)
        # O modelo já está configurado para retornar JSON
        return json.loads(response.text)
    except Exception as e:
        print(f"Erro na IA: {e}")
        return {"error": str(e)}
