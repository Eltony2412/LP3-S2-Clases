# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:16:14 2022

@author: user
"""

#seeeee crea el archivooo, si esta, se sobreescribe y listoo, ponen el contenido
archivo = open("archivo_de_prueba.txt", "wt")
contenido = "Lineal Hola Amigos como estan?\n dddddddd"
archivo.write(contenido)
archivo.close()