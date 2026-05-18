from ListaDuplamente import ListaDuplamente

lista = ListaDuplamente()
lista.imprimir()

lista.add( "João" )
lista.add( "Maria" )
lista.add( "Júlia" )
lista.add( "Abel" )

lista.imprimirReverso()

lista.remover("João")
lista.remover("José")
lista.remover("Abel")

lista.imprimirReverso()


# Exercício: Implemente uma playlist musical utilizando
# lista duplamente encadeada onde o objeto música tem os 
# seguintes atributos:
# título, autor e duração 
# A adição na lista será pela ordem alfabética do título