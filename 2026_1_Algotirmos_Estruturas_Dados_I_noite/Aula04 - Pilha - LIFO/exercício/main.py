from Autor import Autor
from Livro import Livro
from Pilha import Pilha

a1 = Autor("Machado de Assis", 1839 )
a2 = Autor("Clarice Lispector", 1920 )

l1 = Livro("Dom Casmurro", 256 , a1)
l2 = Livro("A hora da Estrela", 88 , a2)
l3 = Livro("Memórias Póstumas de Brás Cubas", 288 , a1)

lifo = Pilha()
lifo.imprimir()
lifo.add( l3 )
lifo.add( l1 )
lifo.add( l2 )

lifo.contLivros("Machado de Assis")
lifo.contLivros("Érico Veríssimo")
lifo.remover()
lifo.remover()
lifo.remover()