from biblia import Biblia
import lib_funcoes

# Se usar somente 'import' devemos acessar a função com 'lib_funcoes.função', para evitar isso usamos esta atribuição:
distrib_pacote = lib_funcoes.distrib_pacote
zeros_esq = lib_funcoes.zeros_esq
acentos = lib_funcoes.acentos

b = Biblia('biblia_NVI.xml')

for idx, livro in enumerate(b.livros()):
    i = idx+1
    for c in range(b.qte_capitulos(livro)):
        cap = c+1 #pq o indice inicia em 0 e o xml em 1
        qte_vers = b.qte_versiculos(livro, cap)
        pacotes = distrib_pacote(qte_vers, 5)
        pos_i = 1
        pos_f = 0
        for p in pacotes:
            pos_i = pos_f + 1
            pos_f = pos_f + p
            nome_arquivo = 'textos/'+zeros_esq(i,2)+'-'+acentos(str.lower(livro))+'-'+zeros_esq(cap)+'-'+zeros_esq(pos_i)+','+zeros_esq(pos_f)+'.txt'
            with open(nome_arquivo, 'w') as f:
                #print('{}, capítulo {}, versículo {} a {}.'.format( b.livro_frm(livro), cap, pos_i, pos_f), file=f)
                b.print_intervalo(livro, cap, pos_i, pos_f, f)
                print('', file=f)
