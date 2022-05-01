#Essa primeira parte do código lê um arquivo contendo os pacotes chamado "pacotes.txt"
#e organiza essas pacotes em uma lista

from regras import regiao, tipo_produto, joias_centro, vendedor_367
pacotes_lista = list()

with open('pacotes.txt', 'r') as arquivo:
    for line in arquivo:
        pacotes_lista.append(line.replace('\n', ''))


## A partir daqui os códigos estão organizados em funções e de acordo com o que se 
## pede em cada item do comando


#1
def coletar_regiao_destino(pacotes_lista):
    """Essa função lista cada destino de todos os pacotes"""
    for pacote in pacotes_lista:
        regiao_destino = regiao(int(pacote[3:6]), 'destino')
        print(f"Região de destino do pacote {pacote}: {regiao_destino}")

#2
def codigo_total_validos(pacotes_lista):
    """Essa função verifica a origem, destino, produto, caso algum desses seja um código
    inválido, o produto não é considerado válido.
    Essa função também verifica se algum pacote de jóias vai para o centro-oeste, se sim,
    não é considerado válido.
    Essa função também verifica se algum pacote é do vendedor 367, se sim, não é considerado
    válido."""
    pacotes_validos = list()
    for pacote in pacotes_lista:
        origem = regiao(int(pacote[0:3]), 'origem')    
        destino = regiao(int(pacote[3:6]), 'destino')
        produto = tipo_produto(int(pacote[12:15]))
        resultado_joias = joias_centro(pacote)
        vendedor = vendedor_367(pacote)

        if origem==False:
            continue
        elif destino==False:      
            continue
        elif produto==False:
            continue
        elif resultado_joias==False:
            continue
        elif vendedor==False:
            continue
       
        pacotes_validos.append(pacote) #caso o pacote consiga chegar nesse parte do codigo
                                       #é porque nenhum variavel acima foi False
                                       #logo, é um pacote válido
          
    print(f"Pacotes válidos: {', '.join(pacotes_validos)}")
    return pacotes_validos

#3
def brinquedos_para_sul(pacotes_lista):
    """Essa funcao verifica se algum brinquedo vai para o Sul"""
    for pacote in pacotes_lista:
        regiao_destino = regiao(int(pacote[3:6]), 'destino')
        produto = tipo_produto(int(pacote[12:15]))
        if regiao_destino=='Sul' and produto=='Brinquedos':
            print(f"{pacote} é um brinquedo que será enviado para o Sul")
        else:
            print(f"{pacote} não é um brinquedo que será enviado para o Sul")

#4
def listar_pacotes_destinos(pacotes_validos):
    "Essa funcao organiza em um dicionario python pacotes validos por regiao de destino"
    "Para conseguir chamar essa função, é preciso primeiro rodar a função chamada codigo_total_validos"
    regioes_dict = {'Norte':[],
                'Nordeste':[],
                'Sul': [],
                'Sudeste': [],
                'Centro-Oeste': []}

    for pacote in pacotes_validos:
        regiao_destino = regiao(int(pacote[3:6]), 'destino')
        if regiao_destino == False:
            continue
        regioes_dict[regiao_destino].append(pacote)

    print('Pacotes organizados por destinos:')
    for key in regioes_dict:
        print(f"{key}: {regioes_dict[key]}")
    return regioes_dict

#5
def listar_pacotes_vendedores(pacotes_validos):
    """Essa função lista cada pacote de cada vendedor encontrado em pacotes validos"""
    "Para conseguir chamar essa função, é preciso primeiro rodar a função chamada codigo_total_validos"
    
    vendedores_dict={}
    for pacote in pacotes_validos:
        vendedor = int(pacote[9:12])
        if vendedores_dict.get(vendedor):
            vendedores_dict[vendedor].append(pacote)
        else:
            vendedores_dict[vendedor] = []
            vendedores_dict[vendedor].append(pacote)

    print('Os vendedores e seus pacotes:')
    for key in vendedores_dict:
        print(f"{key}: {vendedores_dict[key]}")

#6
def relatorio_destinos_produtos(pacotes_validos):
    """Essa função cria um ARQUIVO chamado relatorio_destino_produtos.txt contendo
    cada pacote válido, seu destino e qual o tipo de produto.
    ATENÇÃO: CASO RODE ESSA FUNÇÃO MAIS DE UMA VEZ, APAGAR O ARQUIVO GERADO NA VEZ ANTERIOR. """
    
    regioes_dict = listar_pacotes_destinos(pacotes_validos) #chama a função de numero 4 para listar os destinos, para nao repetir codigo
    with open('relatorio_destino_produtos.txt', 'a') as relatorio:
        for key in regioes_dict: #acessa regiao por regiao
            for pacote in regioes_dict[key]:
                produto = tipo_produto(int(pacote[12:15]))
                relatorio.write(f"{pacote}, {key}, {produto}\n") #escreve no relatorio cada produto de cada regiao

#7
def pacotes_centro_e_norte(pacotes_lista):
    regioes_dict = listar_pacotes_destinos(pacotes_lista) #chama a função de numero 4 para listar os destinos, para nao repetir codigo

    print(f"Podem ir no mesmo caminhão: {regioes_dict['Norte']} e {regioes_dict['Centro-Oeste']}") #mostra na tela os pacotes da região norte e centro-oeste

#8
def ordem_pacotes_centro_norte(pacotes_lista):
    regioes_dict = listar_pacotes_destinos(pacotes_lista) #chama a função de numero 4 para listar os destinos, para nao repetir codigo
    total_centro = len(regioes_dict['Centro-Oeste']) #pega o total de pacotes da regiao centro-oeste pois ela sera listada primeiro e a posicao do norte sera somado a esta

    print("A ordem centro-oeste e depois norte seria esta abaixo:")
    for num, centro in enumerate(regioes_dict['Centro-Oeste']):
        print(f"{num}: {centro}")
    
    for num, norte in enumerate(regioes_dict['Norte']):
        print(f"{num+total_centro}: {norte}") #soma a posição total do centro-oeste porque esta ja foi mostrada

#9
def ordem_pacotes_centro_norte_joias(pacotes_lista):
    regioes_dict = listar_pacotes_destinos(pacotes_lista)
    total_centro = len(regioes_dict['Centro-Oeste'])

    print("A ordem centro-oeste e depois norte seria esta abaixo:")
    for num, centro in enumerate(regioes_dict['Centro-Oeste']):
        print(f"{num}: {centro}")

    norte_sorted = sorted(regioes_dict['Norte'], key=lambda x: (x[12:15]=='001')) #organiza a lista de pacotes do norte deixando os pacotes com final 001 (joias) no final
    for num, norte in enumerate(norte_sorted[::-1]): #a opcao [::-1] no python acessa uma lista de tras para frente, assim, acessando primeiro os pacotes do tipo Joias
        print(f"{num+total_centro}: {norte}")

#10
def codigo_total_invalidos(pacotes_lista):
    pacotes_invalidos = list()
    for pacote in pacotes_lista:
        origem = regiao(int(pacote[0:3]), 'origem')    
        destino = regiao(int(pacote[3:6]), 'destino')
        produto = tipo_produto(int(pacote[12:15]))
        resultado_joias = joias_centro(pacote)
        vendedor = vendedor_367(pacote)

        #esta função utiliza a mesma lógica da função que lista validados, porém se algum deste tens acima for False, é adiciona a lista.
        if origem==False:
            pacotes_invalidos.append(pacote)
        elif destino==False:
            pacotes_invalidos.append(pacote)
        elif produto==False:
            pacotes_invalidos.append(pacote)
        elif resultado_joias==False:
            pacotes_invalidos.append(pacote)
        elif vendedor==False:
            pacotes_invalidos.append(pacote)
            
    
    print(f"Pacotes inválidos: {', '.join(pacotes_invalidos)}")

#coletar_regiao_destino(pacotes_lista)
#pacotes_validos = codigo_total_validos(pacotes_lista)
#brinquedos_para_sul(pacotes_validos)
#listar_pacotes_destinos(pacotes_validos)
#listar_pacotes_vendedores(pacotes_validos)
#relatorio_destinos_produtos(pacotes_validos)
#pacotes_centro_e_norte(pacotes_lista)
#ordem_pacotes_centro_norte(pacotes_lista)
#ordem_pacotes_centro_norte_joias(pacotes_lista)
#codigo_total_invalidos(pacotes_lista)