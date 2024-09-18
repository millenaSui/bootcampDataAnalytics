import numpy as np

# Menus
def menu_modulo():
    print("Módulo:\n(1) Atividades Introdutórias\n(2) Manipulando Arrays\n(3) Cálculo com array\n(4) Sair\n")
    modulo = int(input("Digite o módulo que deseja acessar: "))
    return modulo

def menu_atividades_introdutorias():
    print("Atividade:\n")
    print("    (1) Crie um array com 4 linhas e 3 colunas com valores aleatórios.")
    print("    (2) Crie um array com valores inteiros, 3 linhas e 5 colunas com valores aleatórios.")
    print("    (3) Crie um array com 5 colunas e 10 linhas inicializados com zeros.")
    print("    (4) Crie um array que vá entre 0 e 90 pulando de 4 em 4.")
    print("    (5) Reduza um array (5,7) a apenas uma dimensão.")
    print("    (6) Considerando que você é uma organizadora de um jogo de bingo: Crie um array que irá representar a cartilha desses jogos.\n        Os números das suas cartelas variam entre 1 e 30, e você terá 10 participantes. Cada cartela terá 12 números (4,3).")
    print("    (7) Faça o reshape das suas cartelas para que haja 5 cartelas de 4 linhas e 6 colunas.")
    print("    (8) Retornar aos módulos\n")
    atividade = int(input("Digite a atividade que deseja acessar: "))
    return atividade

def menu_manipulando_arrays(especies):
    print("Atividade:\n")
    print(especies, "\n")
    print("    (1) Explorando Ecossistemas: Como bióloga marinha, me encontrei em uma expedição nas profundezas do Oceano Pacífico, onde \n        estávamos estudando a biodiversidade e a saúde dos recifes de coral. O catálogo abaixo demonstra dados das espécies encontradas,\n        considere a seguinte ordem de colunas:\n")
    print("        ID da espécie, quantidade de representantes encontrados, profundeza, tamanho médio da espécie.\n")
    print("        a. Selecione a segunda coluna com a quantidade de espécies encontradas e adicione em um array as qtd_especies.")
    print("        b. De qtd_especies selecione apenas as primeiras 3 quantidades e print.")
    print("        c. Imprimas as 5 últimas quantidades de espécies.")
    print("        d. Crie um array que contenha apenas os tamanhos das espécies e ordene por ordem crescente.\n")
    print("    (2) Ainda usando o array de espécies marítimas.\n")
    print("        a. Usando um index boolean crie um array que contém os dados da maior espécie encontrada (considerando o seu tamanho), esse valor corresponde ao valor 22.")
    print("        b. Usando fancy index faça um array que contém apenas dados da espécie com ID 297.")
    print("        c. Usando np.where() faça um array com a linha com dados correspondentes a espécie com 105 representantes encontrados.")
    print("        d. Considere a profundeza em que o espécie foi encontrada substitua valores maiores que 60 com 'Profundo'\n")
    print("    (3) Ainda no conjunto 'especies'.\n")
    print("        a. Adicione mais 2 espécies ao array: [[204,10,40,12],[392,11,81,11]].")
    print("        b. Adicionem mais uma coluna no array original agora com o número de espécies encontradas com que indica se o animal enxerga ou não: [0,1,0,0,0,0,1,0,1,1,0,0]\n")
    print("    (4) Retornar aos módulos\n")
    atividade = int(input("Digite a atividade que deseja acessar: "))
    return atividade

def menu_calculo_com_arrays():
    print("Atividade:\n")
    print("    (1) O cliente que teve acidente abaixo da média nos últimos 2 anos, ganhará um desconto no seu seguro. Identifique-os.")
    print("    (2) Qual cliente teve pelo menos 2 anos sem cometer acidentes?")
    print("    (3) Uma professora quer que seus alunos apliquem a função (3x+2y+x*y) em um conjunto de dados. Ela dá dois arrays aos estudantes e pede que seja feita essa operação.")
    print("    (4) Retornar aos módulos\n")
    atividade = int(input("Digite a atividade que deseja acessar: "))
    return atividade

# Seleção de array de acordo com a atividade
def escolhe_atividade_introdutoria(atividade):
    
    ### Atividades Introdutórias
    array_aleatorio = np.random.rand(4,3) #1
    array_inteiros_aleatorios = np.random.randint(0, 10, (3,5)) #2
    array_inicializado_em_zeros = np.zeros((10,5)) #3
    array_pulando_valores = np.arange(0, 90, 4) #4
    array_reduzido = (np.random.rand(5,7)).ravel() #5
    array_cartilha = np.random.randint(1, 30, (10, 4, 3)) #6
    array_cartilha_reformulado = array_cartilha.reshape(5, 4, 6) #7

    # Selecionar array de acordo com a atividade    
    if atividade == 1:
        return array_aleatorio
    elif atividade == 2:
        return array_inteiros_aleatorios
    elif atividade == 3:
        return array_inicializado_em_zeros
    elif atividade == 4:
        return array_pulando_valores
    elif atividade == 5:
        return array_reduzido
    elif atividade == 6:
        return array_cartilha
    elif atividade == 7:
        return array_cartilha_reformulado
    elif atividade > 8:
        return "Atividade não encontrada, tente novamente."

def escolhe_atividade_calculo_com_arrays(atividade, acidentes):
    
    ### Cálculo com Arrays
    cliente_abaixo_media = np.where(np.mean(acidentes, axis=1) < 1)[0] #1
    cliente_nao_acidentou = np.where(np.sum(acidentes == 0, axis=1) >= 2)[0] #2
    array_1 = np.random.randint(0, 10, (3,3)) #3
    array_2 = np.random.randint(0, 10, (3,3)) #3
    resultado_operacao_arrays = (3*array_1) + (2*array_2) + (array_1*array_2) #3

    # Selecionar array de acordo com a atividade
    if atividade == 1:
        return cliente_abaixo_media
    elif atividade == 2:
        return cliente_nao_acidentou
    elif atividade == 3:
        string_resultado_operacao_arrays = f"conjunto 1:\n{array_1}\nconjunto 2:\n{array_2}\nconjunto resultante:\n{resultado_operacao_arrays}"        
        return string_resultado_operacao_arrays
    elif atividade > 4:
        return "Atividade não encontrada, tente novamente."

def escolhe_atividade_manipulando_arrays(atividade, especies):
    
    ### Manipulando Arrays
    qtd_especies = especies[:,1] #1.a
    primeiras_qtd = qtd_especies[:3] #1.b
    ultimas_especies = qtd_especies[-5:] #1.c
    tamanho_especies = especies[:,3] #1.d
    tamanho_especies_ordenado = np.sort(tamanho_especies) #1.d
    maior_especie = especies[especies[:,3] == 22] #2.a
    dados_297 = especies[especies[:,0] == 297] #2.b
    dados_105 = especies[especies[:,1] == 105] #2.c
    marca_profundo = np.where(especies[:,2] > 60, 'Profundo', especies[:,2]) #2.d
    especies_adicionadas = np.append(especies, [[204,10,40,12],[392,11,81,11]], axis=0) #3.a
    especies_enxerga_ou_nao = np.c_[especies_adicionadas, [0,1,0,0,0,0,1,0,1,1,0,0]] #3.b

    # Selecionar array de acordo com a atividade
    if atividade == 1:
        return f"a: {qtd_especies}\nb: {primeiras_qtd}\nc: {ultimas_especies}\nd: {tamanho_especies_ordenado}"    
    elif atividade == 2:
        return f"a: {maior_especie}\nb: {dados_297}\nc: {dados_105}\nd: {marca_profundo}"
    elif atividade == 3:
        return f"a: {especies_adicionadas}\nb: {especies_enxerga_ou_nao}"    
    elif atividade > 4:
        return "Atividade não encontrada, tente novamente."

# Main
def main():

    modulo = 0
    while modulo != 4:
        modulo = menu_modulo() 
        # Atividades Introdutórias    
        if modulo == 1:
            atividade = 0
            while(atividade != 8):
                atividade = menu_atividades_introdutorias()
                print(escolhe_atividade_introdutoria(atividade), "\n")
        # Manipulando Arrays
        elif modulo == 2:
            atividade = 0
            while(atividade != 4):    
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
                atividade = menu_manipulando_arrays(especies)
                print(escolhe_atividade_manipulando_arrays(atividade, especies), "\n")
        # Cálculo com Arrays
        elif modulo == 3:
            atividade = 0
            while(atividade != 4):
                acidentes = np.array([[1,3,2],
                                      [0,1,0],
                                      [2,1,4],
                                      [0,0,0],
                                      [1,1,0]])
                atividade = menu_calculo_com_arrays()
                print(escolhe_atividade_calculo_com_arrays(atividade, acidentes), "\n")

if __name__ == "__main__":
    main()