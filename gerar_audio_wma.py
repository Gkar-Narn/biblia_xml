''' Gera audio de arquivo txt em formato wma, utiliza programas:
    balcon - do Software Balabolka (http://www.cross-plus-a.com/br/balabolka.htm)
    WMAEncode - Encode WMA (https://hydrogenaud.io/index.php/topic,90519.0.html)

    Por padrão de linha de comando o balcon gera em WAV, sendo necessário encode para reduzir tamanho.
'''
import os

balcon_op = '-n Felipe -s -2 -p -2 -v 80 -e 10 -a 10'
pasta_txt = 'textos'
pasta_audio = 'audio'
lista = os.listdir(pasta_txt)

for arq_txt in lista:
    div_arquivo = arq_txt.split('.')
    arq_audio = div_arquivo[0] + '.wma'
    comando = f'balcon -f {pasta_txt}/{arq_txt} {balcon_op} -o | WMAEncode - {pasta_audio}/{arq_audio}'
    os.system(comando)
