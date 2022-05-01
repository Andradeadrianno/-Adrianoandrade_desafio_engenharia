def regiao(trinca, info):
    if 1 <= trinca <= 99:
        resultado = 'Sudeste'
    elif 100 <= trinca <= 199:
        resultado = 'Sul'
    elif 201 <= trinca <= 299:
        resultado = 'Centro-Oeste'
    elif 300 <= trinca <= 399:
        resultado = 'Nordeste'   
    elif 400 <= trinca <= 499:
        resultado = 'Norte' 
    else:  
        return False
    return resultado

def tipo_produto(trinca):
    if trinca == 1:
        produto = 'Jóias'
    elif trinca == 111:
        produto = 'Livros'
    elif trinca == 333:
        produto = 'Eletrônicos'    
    elif trinca == 555:
        produto = 'Bebidas'     
    elif trinca == 888:
        produto = 'Brinquedos'       
    else:
        return False  
    return produto    

def joias_centro(pacote):
    if int(pacote[0:3]) in list(range(201,300)) and pacote[12:15]=='001':
        #Não é possível despachar pacotes contendo jóias tendo como região de origem o Centro-oeste
        return False
    return True

def vendedor_367(pacote):
    if pacote[9:12]=='367':
        #O vendedor 367 está com seu CNPJ inativo
        return False
    return True
