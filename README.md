## Presentacion:

Este repositorio contiene todos los programas de la practica de AyED (1er año UTN) codificados a Python. Tener en cuenta que pueden haber algunos errores, especificamente faltan muchas validaciones de datos, solo se hizo lo especificado en la consigna en la mayoria de casos. Si encuentras algun problema sientete libre de abrir un [Issue](https://github.com/ElMoha943/AyED/issues) o si tienes algun aporte/correxion puedes hacer una [PR](https://github.com/ElMoha943/AyED/pulls).

Si no entiendes algun programa puedes consultarme por [Discord](https://discord.gg/46ME2WY) y con gusto te respondo!

## Problemas comunes con los que me encontre al realizar los ejercicios:

### No se puede operar directamente con los valores ingresador mediante Input()

Los valores guardados en las variables mediante la funcion/metodo Input se guardan como tipo String y no Int/float.
Por esto no se pueden usar directamente para operar (sumas, restas, multiplicaciones, etc).
La solucion a esto es convertir el tipo de variable usando Int(), Float() etc.
Ejemplo:
```python
remu = int(input("ingrese la remuneracion por hora\n"))
```

### Programa crashea al ingresar un valor de otro tipo al convertir el resultado de la funcion input().

Si escribimos por ejemplo: `option=int(input())` e ingresamos un valor que no sea un numero entero, el programa crasheara y mostrara el error: `Error invalid literal for int() with base 10`

Solucion: Utilizar un manejo de excepciones. Ejemplo:
```python
try:
            option=int(input())
except ValueError:
            print("Por favor ingrese un numero entero")
```

### Usar variables en input().

Si escribimos por ejemplo:
```python
input("sueldo del operario N°",i,": ",sueldo)
```
El programa crasheara y mostrara el error: 

`TypeError: input expected at most 1 arguments, got 3”`

Solucion : utilizar el nuevo estilo de formateado de python. Ejemplo:
```python
input("sueldo del operario N°{}: {}".format(i,sueldo))
```
Tambien se puede asi:
```python
input("sueldo del operario N°{numero}: {sueldo}".format(numero=i,sueldo=sueldo))
```

### Python no cuenta con loops do-while

**Podemos emular estos de la siguiente manera:**

Lo que en C seria:
```
do {  
     #statement  
} while (condition);
```
Podemos escribirlo como:
```
while True:  
    #statement  
    if(condition):  
        break  
```
*Nota: la palabra clave "break" termina el bucle actual y sigue ejecutando el programa fuera de este.*
## FAQ

### Q: ¿Qué es **elif**? <br> A: Tambien conocido como "else if" es una estructura similar a meter un if dentro del else de otro if:

Para escribir esto:
```python
if():
  #some code
else:
  if():
    #some more code
```
Se puede escribir como:
```python
if():
  #some code
elif():
  #some more code
```

### Q: ¿Qué es la funcion Range() que usas en los for? <br> A: La funcion devulve una serie de numeros, empezando en 0 por default, e incrementando en 1 (por default), y termina en el numero especificado.

```python
for x in range(2, 30, 3):
  print(x)
```
*Ejemplo de la funcion Range() donde va desde 2 a 30, sumando de a 3 numeros.*

### Q: ¿Donde puedo aprender mas? <br> A: Recomiendo [esta pagina](https://www.w3schools.com/python/default.asp)
