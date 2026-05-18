from Torre import Torre
from Apartamento import Apartamento
from Lista import Lista
from Fila import Fila

t1 = Torre( nome= "Torre B" , end = "Rua B")

ap01 = Apartamento( 1, "101", t1, 1)
ap02 = Apartamento( 2, "102", t1, 2)
ap03 = Apartamento( 3, "103", t1, 3)
ap04 = Apartamento( 4, "104", t1)

lista = Lista()
lista.add( ap01 )
lista.add( ap02 )
lista.add( ap03 )

fila = Fila()
fila.add( ap04 )

def menu():
    print( " ------------------------------------ ")
    print( "| 1) Adicionar Apartamento           |")
    print( "| 2) Liberar Vaga                    |")
    print( "| 3) Imprimir Lista de Apartamentos  |")
    print( "| 4) Imprimir Fila de Apartamentos   |")
    print( "| 0) Sair                            |")
    print( " ------------------------------------ ")
    op = int( input( "Digite sua opção: " ))
    return op

opcao = -1
while opcao != 0:
    opcao = menu()
    if opcao == 1:
        id = int( input( "Digite ID do Ap: " ))
        numero = input( "Digite número do Ap: " )
        novoAp = Apartamento(id, numero, t1)
        fila.add( novoAp )

    if opcao == 2:
        vaga = int( input( "Digite número da Vaga: " ))
        apPerdeuVaga = lista.remover( vaga )
        if apPerdeuVaga: 
            apPerdeuVaga.vaga = None
            fila.add( apPerdeuVaga )
            apGanhouVaga = fila.remover( vaga )
            if apGanhouVaga:
                lista.add( apGanhouVaga )
    if opcao == 3:
        lista.imprimir()
    if opcao == 4:
        fila.imprimir()
    if opcao < 0 or opcao > 4:
        print( "Opção inválida")
    if opcao == 0:
        print( "Bye-Bye!")