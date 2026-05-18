from Musica import Musica
from ListaDuplamente import ListaDuplamente

playlist = ListaDuplamente()

playlist.imprimir()

m1 = Musica("Tempo Perdido", "Renato Russo", 5.5)
m2 = Musica("Faroeste Caboclo", "Renato Russo", 10)
m3 = Musica("Evidência", "José Augusto", 3.5)

playlist.add( m2 )
playlist.add( m1 )
playlist.add( m3 )
playlist.add(  )

playlist.imprimirReverso()