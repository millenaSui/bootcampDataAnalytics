# Utilizando o arquivo: collected_research_people.csv

import pandas as pd
import numpy as np

def corrige_database(db):
    new_db = db.copy()
    
    # remove coluna desnecessária (primeira coluna)
    new_db = new_db.drop(new_db.columns[0], axis=1)

    # renomeia colunas
    new_db.columns = ['Nome', 'Endereco', 'Cidade', 'Estado', 'Telefone', 'Renda_Anual', 'Estado_Civil', 'Idade', 'Numero_Filhos', 'Tipo_Moradia', 'Restricoes_Alimentares', 'Streaming', 'Protetor_Solar_Diario', 'Visita_Praia_Mensal', 'Frequenta_Academia', 'Compra_Le_Livros_Anualmente', 'Quantidade_Livros_Comprados', 'Autor_Favorito', 'Email']
    
    # corrige valores com nomes, mantendo letras acentuadas
    new_db['Nome'] = new_db['Nome'].str.replace(r'[^a-zA-Zà-ÿÀ-ÿ\s]', '', regex=True)
    new_db['Autor_Favorito'] = new_db['Autor_Favorito'].str.replace(r'[^a-zA-Zà-ÿÀ-ÿ\s]', '', regex=True)
    
    # corrige telefone
    new_db['Telefone'] = new_db['Telefone'].str.replace(r'[^0-9() -+]', '*', regex=True)
    new_db.loc[new_db['Telefone'].str.contains(r'[*]', na=False), 'Telefone'] = np.nan

    # corrige estado civil (substitui strings de uma só letra por strings completas)
    new_db.loc[new_db['Estado_Civil'] == "S", 'Estado_Civil'] = "Solteiro"
    new_db.loc[new_db['Estado_Civil'] == "C", 'Estado_Civil'] = "Casado"
    new_db.loc[new_db['Estado_Civil'] == "D", 'Estado_Civil'] = "Divorciado"
    new_db.loc[new_db['Estado_Civil'] == "V", 'Estado_Civil'] = "Viúvo"
                  
    # corrige streaming
    new_db.loc[new_db['Streaming'] == "Netflix e Disney", 'Streaming'] = "Netflix e Disney Plus"
    new_db.loc[new_db['Streaming'] == "Todos", 'Streaming'] = "Globo Play e Netflix e HBO e Disney Plus e Crunchyroll"

    return new_db

def cenario1(db):
    """
    A empresa Carri Construtora contratou a empresa que você trabalha para encontrar 
    possíveis compradores para o seus novos empreendimentos. A empresa quer entender 
    as necessidades dos clientes, e quer informações com:
        - Quais cliente devemos abordar;
        - Qual empreendimento nós devemos mostrá-los;
        - Esse cliente está em busca de investir em um imóvel ou comprar para moradia?
    """

    db_cenario1 = db.copy()
    drop_columns = ['Restricoes_Alimentares', 
                    'Streaming', 
                    'Protetor_Solar_Diario', 
                    'Compra_Le_Livros_Anualmente', 
                    'Quantidade_Livros_Comprados', 
                    'Autor_Favorito']
    db_cenario1.drop(drop_columns, axis=1, inplace=True)
    
    # Tipos proposta
    db_cenario1['Minha_Casa_Minha_Vida'] = True
    db_cenario1['Investimento'] = (db_cenario1['Tipo_Moradia'] == 'Quitada') | (db_cenario1['Tipo_Moradia'] == 'Financiamento')
    
    print(db_cenario1)

def cenario2(db):
    """
    Uma empresa chamada Hillo, é uma empresa que está estudando o mercado e quer encontrar 
    uma parceria com uma empresa de Streeming (netflix, Disney plus etc), mas gostaria de 
    saber quais as empresas dariam o maior retorno de investimento. Eles podem fazer 
    análise de machine learning também com esses dados.
    """    
    db_cenario2 = db.copy()
    drop_columns = ['Tipo_Moradia',
                    'Restricoes_Alimentares', 
                    'Protetor_Solar_Diario', 
                    'Visita_Praia_Mensal', 
                    'Frequenta_Academia', 
                    'Compra_Le_Livros_Anualmente', 
                    'Quantidade_Livros_Comprados', 
                    'Autor_Favorito']
    db_cenario2.drop(drop_columns, axis=1, inplace=True)
    
    # Organiza as empresas de streaming em colunas
    db_cenario2_streaming = db_cenario2['Streaming'].str.get_dummies(sep=' e ')
    db_cenario2 = pd.concat([db_cenario2, db_cenario2_streaming], axis=1)
    
    print(db_cenario2)

def cenario3(db):
    """
    Uma influenciadora digital de bem estar gostaria de analisar possíveis empreendimentos dentro 
    de diferentes propostas que recebe. Essas propostas podem ser excludentes ou somatórias, ou 
    seja, elas podem ser de empresas com o mesmo mercado (empresas concorrentes) ou empresas de
    mercados diferentes (não concorrentes). Exemplo: duas marcas diferentes de chá são concorrentes, 
    mas uma marca de chá e uma marca de bolinhos não são concorrentes.
    """
    db_cenario3 = db.copy()
    drop_columns = ['Tipo_Moradia', 
                    'Streaming']
    db_cenario3.drop(drop_columns, axis=1, inplace=True)

    # Organiza as restrições alimentares em colunas
    restricoes = db_cenario3['Restricoes_Alimentares'].str.get_dummies(sep=' e ').drop('Nenhuma', axis=1)
    db_cenario3 = pd.concat([db_cenario3, restricoes], axis=1)

    # Organiza os autores favoritos em colunas
    autores = db_cenario3['Autor_Favorito'].str.get_dummies(sep=' e ')
    db_cenario3 = pd.concat([db_cenario3, autores], axis=1)

    # Organiza idades em faixas etárias (Jovem, Adulto, Idoso)
    db_cenario3['Jovem'] = (db_cenario3['Idade'] < 30)
    db_cenario3['Adulto'] = (db_cenario3['Idade'] >= 30) & (db_cenario3['Idade'] < 60)
    db_cenario3['Idoso'] = (db_cenario3['Idade'] >= 60)
    
    print(db_cenario3)

def main():
    db = pd.read_csv('collected_research_people.csv')
    database_corrigida = corrige_database(db)
    cenario1(database_corrigida)
    cenario2(database_corrigida)
    cenario3(database_corrigida)
    database_corrigida.to_csv('corrected_collected_research_people.csv', index=False)

if __name__ == '__main__':
    main()
