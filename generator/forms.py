from django import forms

class AnamneseForm(forms.Form):
    # ==========================
    # I. IDENTIFICAÇÃO
    # ==========================
    nome = forms.CharField(label="Nome / Nome social", max_length=200)
    idade = forms.CharField(label="Idade / Data de nascimento", max_length=100)
    sexo_biologico = forms.CharField(label="Sexo biológico", max_length=100, required=False)
    identidade_genero = forms.CharField(label="Identidade de gênero", max_length=100, required=False)
    raca_cor = forms.CharField(label="Raça / Cor / Etnia", max_length=100, required=False)
    naturalidade = forms.CharField(label="Naturalidade", max_length=100, required=False)
    nacionalidade = forms.CharField(label="Nacionalidade", max_length=100, required=False)
    procedencia_proxima = forms.CharField(label="Procedência Próxima", max_length=100, required=False)
    procedencia_remota = forms.CharField(label="Procedência Remota", max_length=100, required=False)
    religiao = forms.CharField(label="Religião", max_length=100, required=False)
    profissao = forms.CharField(label="Profissão", max_length=100, required=False)
    estado_civil = forms.CharField(label="Estado Civil", max_length=100, required=False)
    escolaridade = forms.CharField(label="Escolaridade", max_length=100, required=False)
    face_atendimento = forms.CharField(label="Identificação do responsável pelo atendimento", max_length=200, required=False)

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
    isda_gerais = forms.CharField(label="Sintomas gerais (Febre, Dor, Edema, etc.)", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_pele = forms.CharField(label="Pele e fâneros", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_cabeca = forms.CharField(label="Cabeça", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_pescoco = forms.CharField(label="Pescoço", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    isda_torax = forms.CharField(label="Tórax e Aparelhos Cardio e Respiratório", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_abdome = forms.CharField(label="Abdome e Aparelho Digestório", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_genito_urinario = forms.CharField(label="Aparelho Gênito-Urinário", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_neurologico = forms.CharField(label="Sistema Nervoso", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_saude_mental = forms.CharField(label="Saúde mental / psiquismo", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_locomotor = forms.CharField(label="Sistema Osteo-Articular e Muscular", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_endocrino = forms.CharField(label="Sistema Endócrino", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    isda_imunologico = forms.CharField(label="Sistemas Imunológico e Linfohematopoético", widget=forms.Textarea(attrs={"rows": 3}), required=False)

    # ==========================
    # V. ANTECEDENTES
    # ==========================
    antecedentes_morbidos = forms.CharField(label="Antecedentes mórbidos", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    habitos_vida = forms.CharField(label="Hábitos de vida", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    condicoes_vida = forms.CharField(label="Condições de vida", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    epidemiologia = forms.CharField(label="Antecedentes epidemiológicos", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    vacinacao = forms.CharField(label="Vacinação", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    medicamentos_uso = forms.CharField(label="Medicamentos de uso contínuo", widget=forms.Textarea(attrs={"rows": 2}), required=False)
    antecedentes_familiares = forms.CharField(label="Antecedentes Familiares", widget=forms.Textarea(attrs={"rows": 3}), required=False)

    # ==========================
    # VI. EXAME FÍSICO
    # ==========================
    ef_geral = forms.CharField(label="Exame Físico Geral", widget=forms.Textarea(attrs={"rows": 4}), required=False)
    ef_cabeca_pescoco = forms.CharField(label="Cabeça e Pescoço", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    ef_torax = forms.CharField(label="Exame Físico do Tórax", widget=forms.Textarea(attrs={"rows": 4}), required=False)
    ef_abdome = forms.CharField(label="Exame Físico do Abdome", widget=forms.Textarea(attrs={"rows": 4}), required=False)
    ef_neurologico = forms.CharField(label="Exame Neurológico", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    ef_locomotor = forms.CharField(label="Aparelho Locomotor", widget=forms.Textarea(attrs={"rows": 3}), required=False)

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
