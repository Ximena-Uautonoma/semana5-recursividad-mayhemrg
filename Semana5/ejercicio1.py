"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando iteración.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    pass

def suma_ciclo(n):
    suma = 0
    for x in range(1, n + 1):
        suma += x
    return suma


def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    pass

def suma_recursiva(n):
    if n == 1:
        return [1]
    else:
        return suma_recursiva (n-1) + [n]
    
