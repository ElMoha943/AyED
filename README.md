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
input("Ingrese el sueldo del operario N°",i)
```
El programa crasheara y mostrara el error: 

`TypeError: input expected at most 1 arguments, got 2”`

Solucion : utilizar otro estilo de formateado de python.
Mi favorito es este:
```python
input(f"Ingrese el sueldo del operario N°{i}")
```
Tambien se puede asi:
```python
input("Ingrese el sueldo del operario N°{}".format(i))
```
O asi:
```python
input("Ingrese el sueldo del operario N°{numero}".format(numero=i))
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

### Hacer potencia de un numero

El operador para realizar esto es `**` y no `^` como en la mayoria de lenguajes. Tambien destacar que para dividir numeros con un resultado entero se utiliza `//`.


## FAQ

### Q: ¿Qué es **elif**? <br> A: Es una estructura similar a meter un if dentro del else de otro if:

Para escribir esto:
```python
if(condition1):
  #some code
else:
  if(condition2):
    #some more code
```
Se puede escribir como:
```python
if(condition1):
  #some code
elif(condition2):
  #some more code
```

### Q: ¿Qué es la funcion Range() que usas en los for? <br> A: La funcion devulve una serie de numeros, empezando en 0 por default, e incrementando en 1 (por default), y termina en el numero especificado.

```python
for x in range(2, 30, 3):
  print(x)
```
*Ejemplo de la funcion Range() donde va desde 2 a 30, sumando de a 3 numeros.*

### Q: ¿Qué es \n? <br> A: Sirve para realizar un salto de linea.

### Q: ¿Que tipo de variable debo usar en cada caso? <br> A: este tema requiere una explicacion detallada:

Para determinar que tipo de variable usar debemos tener en cuenta varios factores como:
- **Que se va a guardar en la variable?** un numero entero? un numero decimal? una palabra? una fecha?
- **Que vamos a hacer con ese dato?** Utilizaremos funciones aritmeticas (suma, resta, etc)? usarlo como referencia? o querremos saber que tan largo es, hacerle cambios en posiciones especificas, etc?
- **Nos intereza ahorrar espacio de almacenamiento?** (por ejemplo en programas grandes o al tener espacio limitado como en microchips)

Por norma general y si queremos ir a lo facil se puede tomar como que:
- Numeros enteros (sin coma) utilizaran datos de tipo Integer (int, long, short, byte, etc).
- Numeros decimales utilizaran tipo Float (float, double, decimal).
- 1 solo caracter puede representarse con Char.
- Un conjunto de caracteres, una palabra o frase utilizara tipo String.
- Un '0' o '1' **logico** (true or false) se representara con un tipo Bool.

Notas:
- Numeros enteros solo positivos deberian en cambio utilizar **Unsigned Integer** para ahorrar espacio.

Esto sin embargo puede variar. Ejemplo:<br>
Si se desea guardar el numero de documento de una persona uno podria argumentar que al ser un numero no decimal deberia guardarse en un tipo int. Sin embargo si nos ponemos a analizar el uso del dato que guardaraemos la cosa cambia... Es mas factible que a dicho dato se le quiera tomar una parte (4 ultimos digitos por ejemplo) a que se lo quiera usar para sumarlo a otro numero. En este caso seria mejor un tipo String a un tipo Int, debido a sus funciones. Pero y si quiero por ejemplo buscar todos los dni > a x numero? no es lo mismo hacer x > 500 que x > "500" ("500" > "100000"). O si estoy trabajando con muy poco espacio o simplemente quiero optimizar mi programa? un tipo entero ocupa mucho menos que un tipo string.
<br><br>
Este pequeño ejemplo muestra que no siempre se puede seguir una norma para definir el tipo de variable. El programador debera elegir el que mas se adapte a su caso de uso y sus necesidades.

### Q: ¿Donde puedo aprender mas? <br> A: Recomiendo [esta pagina](https://www.w3schools.com/python/default.asp)
