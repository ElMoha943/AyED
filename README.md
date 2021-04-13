## Presentacion:

Este repositorio contiene todos los programas de la practica de AyED (1er año UTN) codificados a Python. Tener en cuenta que pueden haber algunos errores, especificamente faltan muchas validaciones de datos, solo se hizo lo especificado en la consigna en la mayoria de casos. Si encuentras algun problema sientete libre e abrir un [Issue](https://github.com/ElMoha943/AyED/issues) o si tienes algun aporte/correxion puedes hacer una [PR](https://github.com/ElMoha943/AyED/pulls).

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

### Usar mas de una variable en un print() y/o mostrarla en el medio del mensaje.

Solucion: utilizar el nuevo estilo de formateado de python. Ejemplo:
```python
print("sueldo del operario N°{}: {}".format(i,sueldo))
```
Tambien se puede asi:
```python
print("sueldo del operario N°{numero}: {sueldo}".format(numero=i,sueldo=sueldo))
```
