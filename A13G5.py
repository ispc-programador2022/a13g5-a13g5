#Esta aplicación debe llamar a funciones, cada una en su archivo .py a saber:
#función que muestre cartel de presentación.
#función ing2i, debe permitir el ingreso de 2 valores enteros
#función ing2s, debe permitir el ingreso de 2 valores string
#1- función suma, retorna la suma de 2 parámetros.
#2- función resta, retorna la resta de 2 parámetros.
#3- función producto, retorna el producto de 2 parámetros.
#4- función cociente, retorna el cociente de 2 parámetros.
#5- función módulo, retorna el módulo de 2 parámetros.
#6- función potencia, retorna la potencia del primero elevado al segundo parámetros.
#7- función radicación, retorna la raiz del primero respecto del segundo parámetros.
#9- función p1, retorna el producto de los 2 primero más el 3er parámetros, usando las
#funciones anteriores.
#10- función p1, retorna la suma de los 2 primero por el 3er parámetros, usando las
#funciones anteriores



print ("Bienvenidos al grupo 5 del aula 13")
ing2i1 = int (input ("Ingrese un número: "))
ing2i2 = int (input ("Ingrese un segundo número: "))

ing2s1 = input ("Ingrese un string ")
ing2s2 = input ("Ingrese un segundo string ")

suma = ing2i1 + ing2i2

print ("La suma de ambos números da como resultado: ", suma)

resta = ing2i1 - ing2i2

print ("La resta de ambos números da como resultado: ", resta)

producto = ing2i1 * ing2i2

print ("El producto de ambos números es: ", producto)

cociente = ing2i1 / ing2i2

print ("El cociente de ambos números es: ", cociente)

modulo = ing2i1 % ing2i2

print ("El módulo de ambos números es: ", modulo)

potencia = ing2i1 ** ing2i2

print ("La potencia del primer número respecto del segundo es: ", potencia)

radicacion = pow (ing2i1, ing2i2)

print ("La radicación del primer número con respecto al segundo es: ", radicacion)

numero3 = int (input ("Ingrese un tercer número: "))
p1 = producto + numero3

print ("El producto de los 2 primeros parámetros más el 3ero es: ", p1)

p11 = suma * numero3

print ("La suma de los primeros dos numeros por el tercero da como resultado: ", p11)

