import os
pasta_txt = 'textos'
pasta_audio = 'audio'
balcon_op = '-n Felipe -s -2 -p -2 -v 80 -e 10 -a 10'

arq_txt = '01-genesis-007-016,020.txt'
arq_audio = '01-genesis-001-016,019.wma'
comando = f'balcon -f {pasta_txt}/{arq_txt} {balcon_op} '#-o | WMAEncode - {pasta_audio}/{arq_audio}'

os.system(comando)