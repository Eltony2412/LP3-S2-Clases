# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:39:42 2022

@author: user
"""

import gestion_archivos

while True:
    print ("**MENU**")
    print ("1. Crear archivo")
    print ("2. Eliminar archivo")
    print ("3. Agregar contenido")
    print ("4. Mostrar contenido de archivo")
    print ("5. Salir")
    opc = input ("Ingrese una opcion: ") 


    if opc == "1":
        gestion_archivos.crear_archivo("prueba_mundo.txt", "")        
    elif opc == "2":
        gestion_archivos.eliminar_archivo("prueba_mundo.txt")
    elif opc == "3":
        gestion_archivos.agregar_contenido("prueba_mundo.txt", "Contenido agregado \n TExto prueba")
    elif opc == "4":
        gestion_archivos.leer_archivo("prueba_mundo.txt")
    elif opc == "5":
        break
    else:
        print("OPCION INVALIDA")
        