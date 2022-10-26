# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#IMPORTA PARA USAR EL CAMELCASE
import camelcase

#SE IMPRIME EL NOMBRE SIN MAYUSCULAS
nombre = "elbert antonio luque chavez"
print(f"nombre: {nombre.upper()}")


cam = camelcase.CamelCase()
print ("**CON CAMELCASE**")
#SE IMPRIME EL PRIMER CAMELCASE
print (cam.hump(nombre))

cam2 = camelcase.CamelCase('elberth', 'antonio')
print (cam2.hump(nombre))
#print(f"nombre titulo: {nombre.title()}")
