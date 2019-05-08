# Bíblia XML manipulado em Python
Objeto em Python para manipular Biblias em XML

A intenção do projeto é facilitar a manipulação de Bíblias em XML utilizando Python, tivemos também a pretenção de produzir saídas em texto para convertê-las em áudio.

## A estrutura XML da Bíblia deve estar na forma:
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<biblia tipo="Revista e Atualizada">
<livro nome="Gênesis">
<capitulo numero="1">
<versiculo numero="1">No princípio, criou Deus os céus e a terra.</versiculo>
</capitulo>
</livro>
</biblia>
```

## Descrição dos arquivos:

- biblia.py - Objeto principal para acesso a Bíblia em XML;
- lib_funcoes.py - Biblioteca de funções para facilitar algumas funcionalidades;
- teste_biblia.py - Exemplos de como utilizar o objeto Biblia;
- cliente.py - Exemplo de como gerar arquivos texto da Bíblia em pacotes;
- teste_audio.py - Exemplo de como utilizar a ferramenta Balcon e WMAEncode para gerar áudio de textos;
- gerar_audio_wma.py - Geração de áudio de arquivos txt.

> A saída de áudio utiliza a linguagem instalada no sistema!

> Balcon - Ferramenta do software [Balabolka](http://www.cross-plus-a.com/br/balabolka.htm)

> WMAEncode - Encoder de aúdio [Link](https://hydrogenaud.io/index.php/topic,90519.0.html)

## A FAZER:
- Função para buscar texto(s):
	- Por mais de uma palavra ou regex;
	- Retornar em formato estruturado (com referências);
- Outras funcionalidades...
