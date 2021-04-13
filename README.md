## Problemas comunes con los que me encontre al realizar los ejercicios:

### No se puede operar directamente con los valores ingresador mediante Input()

Los valores guardados en las variables mediante la funcion/metodo Input se guardan como tipo String y no Int/float.
Por esto no se pueden usar directamente para operar (sumas, restas, multiplicaciones, etc).
La solucion a esto es convertir el tipo de variable usando Int(), Float() etc.
Ejemplo:
```python
remu = int(input("ingrese la remuneracion por hora\n"))
```

### Usar mas de una variable en un print() y/o mostrarla en el medio del mensaje.

Solucion: utilizar el nuevo estilo de formateado de python. Ejemplo:
```python
print("sueldo del operario N°{}: {}".format(i,sueldo))
```
Tambien se puede asi:
```python
print("sueldo del operario N°{numero}: {sueldo}".format(numero=i,sueldo=sueldo))
```
