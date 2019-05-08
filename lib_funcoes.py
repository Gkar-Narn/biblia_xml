def zeros_esq(valor, tamanho=3):
    '''Função que acrescenta zeros a esquerda de acordo com a quantidade definida.\n
       Retorna Texto. Padrão '000'\n
       valor = valor que deseja acrescentar zeros a esquerda\n
       tamanho = tamanho da string completa
    '''
    texto = str(valor)
    return (tamanho - len(texto)) * '0' + str(texto)

def distrib_pacote(num, base):
    ''' Distribui uniformemente uma quantidade informada em pacotes de acordo com a base
máxima definida.\nEx: Distribuir 13 unidades em pacotes com conteúdo máximo de 5 por pacote.\n
Retorno: [5, 4, 4]
    '''
    # Definindo qte pacotes
    qte_pacotes = num // base
    if (num % base) != 0: # sobrou resto? então é mais um pacote
        qte_pacotes+=1

    # Definindo conteúdo
    conteudo = num // qte_pacotes
    resto = num % qte_pacotes

    # Preenchendo o conteudo para cada pacote
    pacotes = []
    # se o resto == 0 o conteudo por pacote é a mesma para todos os pacotes
    for i in range(qte_pacotes):
        if resto == 0:
            pacotes.append(conteudo)
        else:
            resto-=1 # retirando 1 do resto
            pacotes.append(conteudo + 1)
    return pacotes

def acentos(texto):
    '''Retira os acentos de um texto'''
    a = ['á','â','ã']
    e = ['é','ê']
    i = ['í','î']
    o = ['ó','ô','õ']
    u = ['ú','û']
    c = ['ç']
    saida = texto
    for v in a:
        saida = saida.replace(v, 'a')
    for v in e:
        saida = saida.replace(v, 'e')
    for v in i:
        saida = saida.replace(v, 'i')
    for v in o:
        saida = saida.replace(v, 'o')
    for v in u:
        saida = saida.replace(v, 'u')
    for v in c:
        saida = saida.replace(v, 'c')
    # Espaço dentro
    saida = saida.replace(' ','')
    return saida
