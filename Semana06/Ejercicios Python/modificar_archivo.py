# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:21:38 2022

@author: user
"""

archivo = open ("texto.txt", "at")

contenido = "\nFuente: RPP"
archivo.write(contenido)

archivo.close()