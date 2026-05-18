def somarAte( n = 0 ):
    if n == 0:
        return 0
    else:
        return n + somarAte( n - 1 )
    
def fatorial( n = 0 ):
    if n == 0:
        return 1
    else:
        return n * fatorial( n - 1 )

print( "Soma de 1 até 5: " , somarAte( 5 ) )
print( "Fatorial de 5 é:  " , fatorial( 5 ) )



# Peça ao usuário que informe um valor e então, usando recursividade ,
# imprima os termos da sequência Fibonacci que são menores que este valor
def fibonacci( a, b , n ):
    if a > n:
        return
    print( a , " - " )
    fibonacci( b , a+b , n )

x = int( input("Digite um valor: " ) )
fibonacci(0 , 1, x)


# Exercícios:
# 1) Implemente uma função recursiva para cálculo de potência
# 2) Implemente uma função recursiva para contagem regressiva
# 3) Implemente uma função recursiva para inverter uma string