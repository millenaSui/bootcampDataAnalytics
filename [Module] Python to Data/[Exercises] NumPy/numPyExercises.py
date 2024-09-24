import numpy as np

### Atividades Introdutórias
def atividades_introdutorias():
    """
    Atividades de introdução aos arrays do numpy.
    """

    # 1. Crie um array com 4 linhas e 3 colunas com valores aleatórios.
    array_aleatorio = np.random.rand(4,3)

    # 2. Crie um array com valores inteiros, 3 linhas e 5 colunas com valores aleatórios.
    array_inteiros_aleatorios = np.random.randint(0, 10, (3,5)) 
    
    # 3. Crie um array com 5 colunas e 10 linhas inicializados com zeros.
    array_inicializado_em_zeros = np.zeros((10,5)) 
    
    # 4. Crie um array que vá entre 0 e 90 pulando de 4 em 4.
    array_pulando_valores = np.arange(0, 90, 4)

    # 5. Reduza um array (5,7) a apenas uma dimensão.
    array_reduzido = (np.random.rand(5,7)).ravel()

    # 6. Considerando que você é uma organizadora de um jogo de bingo: 
    # Os números das suas cartelas variam entre 1 e 30, e você terá 10 participantes. Cada cartela terá 12 números (4,3).
    # Crie um array que irá representar a cartilha desses jogos.
    array_cartilha = np.random.randint(1, 30, (10, 4, 3))
    # 7. Faça o reshape das suas cartelas para que haja 5 cartelas de 4 linhas e 6 colunas.
    array_cartilha_reformulado = array_cartilha.reshape(5, 4, 6)

### Calculo com Arrays
def calculo_com_arrays():
    """
    (Utilizando o array de acidentes)

    Siga as instruções e responda as seguintes perguntas:
    """


    # Array de acidentes
    acidentes = np.array([[1,3,2],
                [0,1,0],
                [2,1,4],
                [0,0,0],
                [1,1,0]])

    # 1. O cliente que teve acidente abaixo da média nos últimos 2 anos, ganhará um desconto no seu seguro. Identifique-os.
    cliente_abaixo_media = np.where(np.mean(acidentes, axis=1) < 1)[0]

    # 2. Qual cliente teve pelo menos 2 anos sem cometer acidentes?
    cliente_nao_acidentou = np.where(np.sum(acidentes == 0, axis=1) >= 2)[0] #2

    # 3. Uma professora quer que seus alunos apliquem a função (3x+2y+x*y) em um conjunto de dados. 
    # Ela dá dois arrays aos estudantes e pede que seja feita essa operação.
    array_1 = np.random.randint(0, 10, (3,3)) #3
    array_2 = np.random.randint(0, 10, (3,3)) #3
    resultado_operacao_arrays = (3*array_1) + (2*array_2) + (array_1*array_2) #3

### Manipulando Arrays
def manipulando_arrays():
    """
    (Utilizando o array de espécies)
    
    Siga as instruções e responda as seguintes perguntas:
    """


    # Array de espécies
    especies = np.array([[747,89,33,5],
                [623,123,32,13],
                [501,22,49,2],
                [116,101,42,10],
                [297,56,69,22],
                [613,64,27,7],
                [295,84,29,14],
                [692,105,72,16],
                [229,103,35,5],
                [374,124,70,1]])

    # 1. Explorando Ecossistemas: Como bióloga marinha, me encontrei em uma expedição nas profundezas do 
    # Oceano Pacífico, onde estávamos estudando a biodiversidade e a saúde dos recifes de 
    # coral. O catálogo abaixo demonstra dados das espécies encontradas,
    # considere a seguinte ordem de colunas:
    
    # ID da espécie, quantidade de representantes encontrados, profundeza, tamanho médio da espécie.

    # a. Selecione a segunda coluna com a quantidade de espécies encontradas e adicione em um array as qtd_especies.
    qtd_especies = especies[:,1]
    # b. De qtd_especies selecione apenas as primeiras 3 quantidades e print.
    primeiras_qtd = qtd_especies[:3] 
    # c. Imprimas as 5 últimas quantidades de espécies.
    ultimas_especies = qtd_especies[-5:]
    # d. Crie um array que contenha apenas os tamanhos das espécies e ordene por ordem crescente.
    tamanho_especies = especies[:,3]
    tamanho_especies_ordenado = np.sort(tamanho_especies)

    # 2. Ainda usando o array de espécies marítimas.
    # a. Usando um index boolean crie um array que contém os dados da maior espécie encontrada 
    # (considerando o seu tamanho), esse valor corresponde ao valor 22.
    maior_especie = especies[especies[:,3] == 22]
    # b. Usando fancy index faça um array que contém apenas dados da espécie com ID 297.
    dados_297 = especies[especies[:,0] == 297]
    # c. Usando np.where() faça um array com a linha com dados correspondentes a espécie com 105 representantes encontrados.
    dados_105 = especies[especies[:,1] == 105]
    # d. Considere a profundeza em que o espécie foi encontrada substitua valores maiores que 60 com 'Profundo'
    marca_profundo = np.where(especies[:,2] > 60, 'Profundo', especies[:,2])

    # 3. Ainda no conjunto 'especies'.
    # a. Adicione mais 2 espécies ao array: [[204,10,40,12],[392,11,81,11]].
    especies_adicionadas = np.append(especies, [[204,10,40,12],[392,11,81,11]], axis=0)
    # b. Adicionem mais uma coluna no array original agora com o número de espécies encontradas com que indica se o animal enxerga ou não: [0,1,0,0,0,0,1,0,1,1,0,0]
    especies_enxerga_ou_nao = np.c_[especies_adicionadas, [0,1,0,0,0,0,1,0,1,1,0,0]]

def main():
    atividades_introdutorias()
    calculo_com_arrays()
    manipulando_arrays()

if __name__ == "__main__":
    main()