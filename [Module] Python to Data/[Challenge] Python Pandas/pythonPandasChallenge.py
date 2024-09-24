import pandas as pd
import numpy as np
from tabulate import tabulate

"""
Você é uma pesquisadora que está tentando entender melhor qual o impacto do estilo de 
vida de uma pessoa na sua qualidade de sono, por isso fez a coleta dos dados de sobre 
373 pessoas, onde foram recolhidas 12 características para cada uma delas. Por competência 
a sua pesquisa foi bem controlada e você não tem dados faltosos na sua base. Chegou 
o momento de você fazer sua análise e responder algumas perguntas.
"""

### 1. Ao visualizar a base você percebeu que seria melhor alterar o nome de algumas colunas. 
###    Mude o ‘ID’ para ‘Identificador’, corrija o nome da coluna que indica a pressão sanguínea, 
###    mude a coluna ‘Ocupação’ para ‘Profissão’, a coluna ‘Categoria BMI’ está em parte em inglês, 
### substitua para ‘Categoria IMC’.
def altera_nomes_colunas(database):
    database.rename(columns={
        'ID': 'Identificador',
        'Pressão sanguíneaaaa': 'Pressão sanguínea',
        'Ocupação': 'Profissão',
        'Categoria BMI': 'Categoria IMC'
    }, inplace=True)

### 2. Qual é a média, a moda e a mediana de horas de sono para cada uma das profissões? 
###    [‘mean’, np.median, pd.Series.mod]
def media_moda_mediana_de_horas_sono_por_profissao(database):
    horas_sono_por_profissao = database.groupby('Profissão')['Duração do sono'].agg(['mean', 'median', lambda x: x.mode()[0]])

    # Renomeia colunas para corresponder ao requisitado
    horas_sono_por_profissao = horas_sono_por_profissao.rename(columns={
        'mean': 'média',
        'median': 'mediana',
        '<lambda_0>': 'moda'
    })
    # Retorna tabela formatada com tabulate
    return tabulate(horas_sono_por_profissao, headers='keys', tablefmt='fancy_grid', showindex=True)

### 3. Das pessoas que atuam com engenharia de software qual a porcentagem de obesos?
def porcentagem_obesos_engenharia_de_software(database):
    # Filtra engenheiros de software por coluna da profissão e calcula porcentagem de obesos
    engenheiros_de_software = database[database['Profissão'] == 'Eng. de Software']
    porcentagem_obesos = (engenheiros_de_software['Categoria IMC'] == 'Obesidade').mean() * 100

    # Cria a tabela com a porcentagem resultante
    porcentagem_obesos = [['Porcentagem', f"{porcentagem_obesos:.2f}%"]]

    return tabulate(porcentagem_obesos, tablefmt='fancy_grid')

### 4. De acordo com os dados, advogar ou ser representante de vendas faz você dormir 
###    menos? (Use o método ‘isin’, considere a média)
def advogados_e_representantes_dormem_menos(database):
    # Calcula a média de sono de todas as profissões individualmente
    media_sono_geral = database.groupby('Profissão')['Duração do sono'].mean().mean()

    # Filtra o DataFrame para incluir apenas advogados e representantes de vendas e calcula a média de sono desses
    filtragem_advogados_representantes = database[database['Profissão'].isin(['Advogado(a)', 'Representante de vendas'])]
    media_sono_advogados_e_representantes = filtragem_advogados_representantes['Duração do sono'].mean()

    # Verifica se há impacto negativo no sono de advogados e representantes
    impacto_negativo = 'SIM' if media_sono_advogados_e_representantes < media_sono_geral else 'NÃO'

    # Cria a tabela comparativa com os índices e valores correspondentes
    tabela_comparativa = [
        ['Média de sono geral', f"{media_sono_geral:.2f}"],
        ['Média de sono advogados e representantes', f"{media_sono_advogados_e_representantes:.2f}"],
        ['Há impacto negativo', impacto_negativo]
    ]

    # Retorna a tabela formatada
    return tabulate(tabela_comparativa, tablefmt='fancy_grid')

### 5. Entre quem fez enfermagem e quem fez medicina, quem tem menos horas de sono? 
###    (Use o método ‘isin’, considere a média)
def menos_horas_sono_enfermeiros_e_medicos(database):
    # Filtra enfermeiros e calcula a média de sono da profissão
    filtragem_enfermeiros = database[database['Profissão'].isin(['Enfermeiro(a)'])]
    media_sono_enfermeiros = filtragem_enfermeiros['Duração do sono'].mean()

    # Filtra médicos e calcula a média de sono da profissão
    filtragem_medicos = database[database['Profissão'].isin(['Médico(a)'])]
    media_sono_medicos = filtragem_medicos['Duração do sono'].mean()

    if media_sono_medicos < media_sono_enfermeiros:
        menos_horas_de_sono = 'Médicos(as)'
    elif media_sono_enfermeiros < media_sono_medicos:
        menos_horas_de_sono = 'Enfermeiros(as)'
    else:
        menos_horas_de_sono = 'Ambos'

    # Cria a tabela comparativa com os índices e valores correspondentes
    tabela_comparativa = [
        ['Média de sono médicos(as)', f"{media_sono_medicos:.2f}"],
        ['Média de sono enfermeiros(as)', f"{media_sono_enfermeiros:.2f}"],
        ['Menos horas de sono', menos_horas_de_sono]
    ]

    # Retorna a tabela formatada
    return tabulate(tabela_comparativa, tablefmt='fancy_grid')

### 6. Faça um subconjunto com as colunas Identificador, Gênero, Idade,
###    Pressão sanguínea e Frequência cardíaca.
def desenvolve_subconjunto(database):
    # Filtra database para incluir apenas as colunas requisitadas
    subconjunto = database[['Identificador', 'Gênero', 'Idade', 'Pressão sanguínea', 'Frequência cardíaca']]

    return tabulate(subconjunto, headers='keys', tablefmt='fancy_grid')

### 7. Descubra qual a profissão menos frequente no conjunto. (Use value_counts)
def profissao_menos_frequente(database):
    contagem_valores_de_profissao = database['Profissão'].value_counts()
    profissao_menos_frequente = contagem_valores_de_profissao.idxmin()

    return tabulate([['Profissão menos frequente', profissao_menos_frequente]], tablefmt='fancy_grid')

### 8. Quem tem maior pressão sanguínea média, homens ou mulheres? (Considere a média)
def maior_pressao_sanguinea_media_por_genero(database):
    # Separa a parte sistólica da pressão sanguínea e a converte para um valor inteiro
    database['Pressão sistólica'] = database['Pressão sanguínea'].apply(lambda x: int(x.split('/')[0]))

    # Filtra homens e calcula a média da pressão sistólica
    filtragem_homens = database[database['Gênero'].isin(['Homem'])]
    media_pressao_homens = filtragem_homens['Pressão sistólica'].mean()
    # Filtra mulheres e calcula a média da pressão sistólica
    filtragem_mulheres = database[database['Gênero'].isin(['Mulher'])]
    media_pressao_mulheres = filtragem_mulheres['Pressão sistólica'].mean()

    if media_pressao_homens > media_pressao_mulheres:
        genero_maior_pressao = 'Homem'
    elif media_pressao_mulheres > media_pressao_homens:
        genero_maior_pressao = 'Mulher'
    else:
        genero_maior_pressao = 'Ambos'

    # Tabela comparativa com os índices e valores correspondentes
    tabela_comparativa = [
        ['Média de pressão sanguínea homens', f"{media_pressao_homens:.2f}"],
        ['Média de pressão sanguínea mulheres', f"{media_pressao_mulheres:.2f}"],
        ['Gênero com maior pressão sanguínea média', genero_maior_pressao]
    ]

    return tabulate(tabela_comparativa, tablefmt='fancy_grid')

### 9. É predominante entre os participantes dormir 8 horas por dia? 
###    (considere usar Moda como medida)
def moda_duracao_sono(database):
    # Calcula a moda da duração do sono e verifica se é maior ou igual a 8 horas
    moda_duracao_sono = database['Duração do sono'].mode()[0]
    oito_horas_por_dia = 'SIM' if moda_duracao_sono >= 8 else 'NÃO'

    # Tabela comparativa com os índices e valores correspondentes
    tabela_comparativa = [
        ['Moda da duração do sono', moda_duracao_sono],
        ['Dormir 8 horas por dia é predominante?', oito_horas_por_dia]
    ]

    return tabulate(tabela_comparativa, tablefmt='fancy_grid')

### 10. Pessoas com frequências cardíacas acima de 70 dão mais passos que pessoas 
###     com frequência cardíaca menor ou igual a 70? (Use a média)
def passos_diarios_frequencia_cardiaca(database):
    # Converte a coluna de frequência cardíaca para valores numéricos
    database['Frequência cardíaca'] = pd.to_numeric(database['Frequência cardíaca'], errors='coerce')

    # Calcula a média de passos diários para frequência cardíaca acima e abaixo de 70
    acima_de_70 = database[database['Frequência cardíaca'] > 70]['Passos diários'].mean()
    abaixo_de_70 = database[database['Frequência cardíaca'] <= 70]['Passos diários'].mean()

    # Faz a comparação entre as médias de passos diários
    if acima_de_70 > abaixo_de_70:
        mais_passos = 'Acima de 70'
        resposta = 'SIM'
    elif abaixo_de_70 > acima_de_70:
        mais_passos = 'Abaixo de 70'
        resposta = 'NÃO'
    else:
        mais_passos = 'Ambos'
        resposta = 'Mesma quantidade de passos'

    # Tabela comparativa com os índices e valores correspondentes
    tabela_comparativa = [
        ['Média de passos diários com frequência cardíaca acima de 70', f"{acima_de_70:.2f}"],
        ['Média de passos diários com frequência cardíaca abaixo de 70', f"{abaixo_de_70:.2f}"],
        ['Mais passos diários', mais_passos],
        ['Pessoas com frequência cardíaca acima de 70 dão mais passos?', resposta]
    ]

    return tabulate(tabela_comparativa, tablefmt='fancy_grid')

def main():
    # Carrega base de dados
    database = pd.read_csv('./saude_do_sono_estilo_vida.csv')

    # Altera nomes das colunas com as correções requisitadas
    altera_nomes_colunas(database)

    # Imprime resultados das funções elaboradas para a resolução dos tópicos
    print(f"\nMédia, moda e mediana das horas de sono para cada profissão:")
    print(media_moda_mediana_de_horas_sono_por_profissao(database))

    print(f"\nQual a porcentagem de obesos dentre as pessoas que atuam em engenharia de software?")
    print(porcentagem_obesos_engenharia_de_software(database))

    print(f"\nAdvogar ou ser representante de vendas faz você dormir menos?")
    print(advogados_e_representantes_dormem_menos(database))

    print(f"\nDentre enfermeiros(as) e médicos(as), quem tem menos horas de sono?")
    print(menos_horas_sono_enfermeiros_e_medicos(database))

    print("\nSubconjunto com colunas requisitadas (Identificador, Gênero, Idade, Pressão Sanguínea e Frequência Cardíaca):")
    print(desenvolve_subconjunto(database))

    print(f"\nQual a profissão menos frequente no conjunto?")
    print(profissao_menos_frequente(database))

    print(f"\nQual o gênero com maior pressão sanguínea média?")
    print(maior_pressao_sanguinea_media_por_genero(database))

    print(f"\nÉ predominante entre os participantes dormir 8 horas por dia?")
    print(moda_duracao_sono(database))

    print(f"\nPessoas com frequência cardíaca acima de 70 dão mais passos que pessoas com frequência cardíaca menor ou igual a 70?")
    print(passos_diarios_frequencia_cardiaca(database))

if __name__ == '__main__':
    main()