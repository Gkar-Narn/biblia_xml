from biblia import Biblia

b = Biblia('biblia_RA.xml')

print(b.versao())
print(b.livros())

# Não precisa de print() pois a função já traz esta funcionalidade.
b.print_capitulo('Salmos',8)
b.print_intervalo('Mateus',7,7,8)
