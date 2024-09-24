from pandas import read_csv
import pandas as pd

### Dataframe e ordenação
def dataframe_e_ordenacao():
    """
    (Utilizando o arquivo carros.csv) 
    
    Siga as seguintes instruções:
    """

    # 1. Faça o upload do CSV carros.csv
    df = read_csv('carros.csv')
    
    # 2. Print seu head com 10 linhas
    print(df.head(10))
    # 3. Agora print as colunas e index do dataframe
    print(df.columns)
    print(df.index)
    
    # 4. Faça um sort decrescente no dataframe pelo estado com maior quantidade de carros
    df.sort_values('Quant Carros', ascending=False)
    
    # 5. Descubra qual a proporção de carro para a população de cada estado e insira em uma nova coluna
    proporcao = df['Quant Carros'] / df['População do Estado']
    df['Proporção Carros por População'] = proporcao

    # 6. Faça um dataframe com Estado e proporção de carro por habitante
    new_df = df[['Estado', 'Proporção Carros por População']]

### Agregação de dados
def agregacao_de_dados():
    """
    (Utilizando o arquivo dados_concurso.csv)

    Responda as seguintes perguntas:
    """

    df = read_csv('dados_concurso.csv')
    # 7. Qual a média de idade por estado?
    df['Data de Nascimento'] = pd.to_datetime(df['Data de Nascimento'], errors='coerce')
    media_idade = df.groupby('Estado')['Data de Nascimento'].mean()
    print("Media de idade por região: ", media_idade)

    # 8. Qual é a porcentagem de pessoas com deficiência?
    porcentagem_deficiencia = df['Deficiência'].value_counts(normalize=True).get("Sim", 0)
    print("Porcentagem de pessoas com deficiência: ", porcentagem_deficiencia)
    
    # 9. Quantas pessoas são do estado do Piauí?
    pessoas_piaui = df[df['Estado']=='PI']['Número de Inscrição'].count()
    print("Quantidade de pessoas do estado do Piauí: ", pessoas_piaui)

### Indexação e Fatiamento
def indexacao_e_fatiamento():
    """
    (Utilizando o arquivo dados_concurso.csv)
    
    Responda as seguintes perguntas:
    """

    df = read_csv('dados_concurso.csv')

    # 10. Quantas pessoas são do estado do Piauí?
    pessoas_piaui = df[df['Estado']=='PI']['Número de Inscrição'].count() 
    print("Quantidade de pessoas do estado do Piauí: ", pessoas_piaui)

    # 11. Quantas do ES são so sexo feminino?
    pessoas_es_feminino = df[(df['Estado']=='ES') & (df['Sexo']=='Feminino')]['Número de Inscrição'].count()
    print("Quantidade de pessoas do ES do sexo feminino: ", pessoas_es_feminino)

    # 12. Quantas pessoas nasceram antes de 1995?
    pessoas_nascidas_antes_1995 = df[df['Data de Nascimento'] < '1995-01-01']['Número de Inscrição'].count()
    print("Quantidade de pessoas nascidas antes de 1995: ", pessoas_nascidas_antes_1995)

    # 13. Retorne os dados dos inscritos com as colunas: nº inscrição, nome e idade.
    dados_inscritos = df[['Número de Inscrição', 'Nome', 'Data de Nascimento']]
    print("Dados dos inscritos: ", dados_inscritos)

### Valores faltosos
def valores_faltosos():
    """
    Siga as seguintes instruções:
    """

    df_carros = read_csv('carros.csv')
    df_concurso = read_csv('dados_concurso.csv')

    # 14. Para os valores faltosos coloque:
    #     a. Se string: Falta informação
    #     b. Se número: mediana
    falta_informacao = 'Falta informação'
    
    df_carros.fillna({
        'Região': falta_informacao, 
        'Estado': falta_informacao, 
        'Quant Carros': df_carros['Quant Carros'].median(), 
        'Quant Carros Família com Filhos': df_carros['Quant Carros Família com Filhos'].median(), 
        'População do Estado': df_carros['População do Estado'].median(),
        'Carros por habitante': df_carros['Carros por habitante'].median()
        }, inplace=True)
    
    df_concurso.fillna({
        'Número de Inscrição': falta_informacao, 
        'Data de Nascimento': falta_informacao, 
        'Data de Inscrição': falta_informacao, 
        'Cidade': falta_informacao,
        'Estado': falta_informacao,
        'Sexo': falta_informacao,
        'Deficiência': falta_informacao,
        'Nome': falta_informacao,
        'Sobrenome': falta_informacao,
        'Escolaridade': falta_informacao,
        }, inplace=True)

    # 15. Plote a porcentagem de dados faltosos para cada coluna.
    df_carros.isnull().mean().plot(kind='bar')
    df_concurso.isnull().mean().plot(kind='bar')

def main():
    dataframe_e_ordenacao()
    agregacao_de_dados()
    indexacao_e_fatiamento()
    valores_faltosos()

if __name__ == '__main__':
    main()