from django import forms

class AnamneseForm(forms.Form):
    # ==========================
    # CABEÇALHO (NOVO)
    # ==========================
    hospital_name = forms.CharField(label="Nome do Hospital", max_length=200, required=True)
    data_aten = forms.CharField(label="Data do Atendimento", max_length=50, required=True)
    aluno_names = forms.CharField(label="Profissional(ais) / Aluno(s)", max_length=300, required=True)

    # ==========================
    # I. IDENTIFICAÇÃO
    # ==========================
    nome = forms.CharField(label="Nome / Iniciais", max_length=200, required=False)
    nome_social = forms.CharField(label="Nome Social", max_length=200, required=False)
    idade = forms.CharField(label="Idade", max_length=100, required=False)
    data_nascimento = forms.CharField(label="Data de Nascimento", max_length=100, required=False)
    sexo_biologico = forms.CharField(label="Sexo biológico", max_length=100, required=False)
    raca_cor = forms.CharField(label="Raça / Cor / Etnia", max_length=100, required=False)
    estado_civil = forms.CharField(label="Estado Civil", max_length=100, required=False)
    religiao = forms.CharField(label="Religião", max_length=100, required=False)
    escolaridade = forms.CharField(label="Escolaridade", max_length=100, required=False)
    profissao = forms.CharField(label="Profissão / Ocupação", max_length=100, required=False)
    aposentadoria = forms.CharField(label="Tempo de aposentadoria", max_length=100, required=False)
    naturalidade = forms.CharField(label="Naturalidade", max_length=100, required=False)
    nacionalidade = forms.CharField(label="Nacionalidade", max_length=100, required=False)
    procedencia_prox = forms.CharField(label="Procedência Próxima", max_length=100, required=False)
    procedencia_rem = forms.CharField(label="Procedência Remota", max_length=100, required=False)
    residencia_atual = forms.CharField(label="Residência atual (Cidade/Bairro)", max_length=200, required=False)
    tempo_residencia = forms.CharField(label="Tempo em que reside no local", max_length=100, required=False)

    # Campos que existiam no bloco legado mas agora seguem o PDF:
    identidade_genero = forms.CharField(label="Identidade de gênero", max_length=100, required=False)

    # ==========================
    # II. QUEIXA PRINCIPAL E DURAÇÃO (QD)
    # ==========================
    queixa_principal = forms.CharField(label="Queixa principal", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    
    # ==========================
    # III. HISTÓRIA PREGRESSA DA MOLÉSTIA ATUAL (HPMA)
    # ==========================
    hpma = forms.CharField(label="História Pregressa da Moléstia Atual", widget=forms.Textarea(attrs={"rows": 5}), required=False)

    # ==========================
    # IV. INTERROGATÓRIO SOBRE OS SINTOMAS DOS DEMAIS APARELHOS (ISDA)
    # ==========================
    isda_gerais = forms.CharField(label="Sintomas gerais", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_pele = forms.CharField(label="Pelos e fâneros", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_cabeca = forms.CharField(label="Cabeça", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_olhos = forms.CharField(label="Olhos", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_nariz = forms.CharField(label="Nariz", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_ouvidos = forms.CharField(label="Ouvidos", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_boca = forms.CharField(label="Boca", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_garganta = forms.CharField(label="Garganta", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_pescoco = forms.CharField(label="Pescoço", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_torax = forms.CharField(label="Tórax e Aparelhos Cardiorrespiratórios", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_abdome = forms.CharField(label="Abdome e Aparelho Digestório", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_urinario = forms.CharField(label="Sintomas Urinários", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_repro_fem = forms.CharField(label="Aparelho Reprodutor Feminino", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_repro_masc = forms.CharField(label="Aparelho Reprodutor Masculino", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_mamas = forms.CharField(label="Mamas", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_neurologico = forms.CharField(label="Sistema Nervoso / Neurológico", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_saude_mental = forms.CharField(label="Saúde mental / psiquismo", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_locomotor = forms.CharField(label="Aparelho Locomotor", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_endocrino = forms.CharField(label="Sistema Endócrino", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_imunologico = forms.CharField(label="Sistemas Imunológico e Linfohematopoético", widget=forms.Textarea(attrs={"rows": 2}), required=False)

    # ==========================
    # V. ANTECEDENTES
    # ==========================
    ant_morbidos = forms.CharField(label="Antecedentes mórbidos", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    habitos_vida = forms.CharField(label="Hábitos de vida", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    condicoes_vida = forms.CharField(label="Condições de vida", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    epidemiologia = forms.CharField(label="Antecedentes epidemiológicos", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    vacinacao = forms.CharField(label="Vacinação", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    medicamentos_uso = forms.CharField(label="Medicamentos de uso contínuo", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ant_familiares = forms.CharField(label="Antecedentes Familiares", widget=forms.Textarea(attrs={"rows": 3}), required=False)

    # ==========================
    # VI. EXAME FÍSICO (DETALHADO)
    # ==========================
    # VII - Exame Físico Geral
    ef_estado_geral = forms.CharField(label="Avaliação do estado geral", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_pa = forms.CharField(label="PA", max_length=100, required=False)
    ef_fc = forms.CharField(label="FC", max_length=100, required=False)
    ef_t = forms.CharField(label="T", max_length=100, required=False)
    ef_fr = forms.CharField(label="FR", max_length=100, required=False)
    ef_peso = forms.CharField(label="Peso", max_length=100, required=False)
    ef_altura = forms.CharField(label="Altura", max_length=100, required=False)
    ef_imc = forms.CharField(label="IMC", max_length=100, required=False)
    ef_consciencia = forms.CharField(label="Avaliação do nível de consciência", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_hidratacao = forms.CharField(label="Avaliação do estado de hidratação", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_nutricao = forms.CharField(label="Avaliação do estado de nutrição", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_mucosas = forms.CharField(label="Mucosas", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_facies = forms.CharField(label="Fácies", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_atitude = forms.CharField(label="Atitude", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_anexos_pelos = forms.CharField(label="Pelos", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_anexos_unhas = forms.CharField(label="Unhas", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_pele = forms.CharField(label="Pele", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_linfonodos = forms.CharField(label="Linfonodos", widget=forms.Textarea(attrs={"rows": 2}), required=False)

    # Exame físico do aparelho respiratório
    ef_resp_insp_est = forms.CharField(label="Inspeção Estática", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_resp_insp_din = forms.CharField(label="Inspeção Dinâmica", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_resp_percussao = forms.CharField(label="Percussão", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_resp_palpacao = forms.CharField(label="Palpação", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_resp_ausculta = forms.CharField(label="Ausculta", widget=forms.Textarea(attrs={"rows": 2}), required=False)

    # Exame físico do aparelho circulatório
    ef_circ_inspecao = forms.CharField(label="Inspeção", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_circ_palpacao = forms.CharField(label="Palpação", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_circ_ausculta = forms.CharField(label="Ausculta", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_circ_arterias = forms.CharField(label="Artérias", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    ef_circ_pulsos = forms.CharField(label="Pulsos", widget=forms.Textarea(attrs={"rows": 2}), required=False)

    # VIII - Exame Físico Especial (DETALHADO)
    ef_cabeca_detalhe = forms.CharField(label="Cabeça (Crânio, Olhos, Nariz, Ouvidos, Boca)", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    ef_pescoco_detalhe = forms.CharField(label="Pescoço e Tireoide", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    ef_abdome_especial = forms.CharField(label="Abdome (Fígado, Baço, Rins, Aorta)", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    ef_neuro_detalhe = forms.CharField(label="Exame Neurológico", widget=forms.Textarea(attrs={"rows": 4}), required=False)
    ef_locomotor_detalhe = forms.CharField(label="Aparelho Locomotor", widget=forms.Textarea(attrs={"rows": 4}), required=False)

    # ==========================
    # VII. HIPÓTESES DIAGNÓSTICAS, EXAMES, PLANO TERAPÊUTICO, PROGNÓSTICO
    # ==========================
    hipoteses = forms.CharField(label="Hipóteses Diagnósticas", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    exames = forms.CharField(label="Exames complementares", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    plano_terapeutico = forms.CharField(label="Plano terapêutico", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    prognostico = forms.CharField(label="Prognóstico", widget=forms.Textarea(attrs={"rows": 3}), required=False)

    def __init__(self, *args, **kwargs):
        super(AnamneseForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
