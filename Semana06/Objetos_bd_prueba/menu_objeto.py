# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 20:28:56 2022

@author: user
"""

import Metodos_objeto

while True:
    print ("\n**Menu**")
    print ("1. Listar objeto")
    print ("2. Agregar objeto")
    print ("3. Modificar objeto")
    print ("4. Eliminar objeto")
    print ("5. Salir")
    
    opc = input ("Ingrese un opcion: ")
    
    if opc == "1":
        Metodos_objeto.listar_base()
    elif opc == "2":
        nombre = input ("Ingrese objeto nuevo: ")
        cantidad = input ("Ingrese cantidad: ")
        estado = input ("Ingrese estado: ")
        Metodos_objeto.agregar_base(nombre, cantidad, estado)
    elif opc == "3":
        indice = input ("Ingrese indice a modificar: ")
        nombreNew = input ("Ingrese nombre nuevo: ")
        cantidadNew = input ("Ingrese cantidad nueva: ")
        estadoNew = input ("Ingrese estado nuevo: ")
        Metodos_objeto.editar_objeto(indice, nombreNew, cantidadNew, estadoNew)
    elif opc == "4":
        Metodos_objeto.listar_base()
        indice = input ("Ingrese objeto a eliminar: ")
        Metodos_objeto.eliminar_objeto(indice)
    elif opc == "5":
        break
    else:
        print ("Opcion invalida")
        
        