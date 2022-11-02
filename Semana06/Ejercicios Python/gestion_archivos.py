# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:33:33 2022

@author: user
"""
#ACTIVIDAD DE ARCHIVOS

def crear_archivo(nombre, contenido):
    
    archivo = open(nombre, "wt")
    archivo.write(contenido)
    archivo.close()
    
def eliminar_archivo(nombre):
    import os
    os.remove(nombre)
    
def agregar_contenido(nombre, contenido):
    archivo = open (nombre, "at")
    archivo.write(contenido)
    archivo.close()

def leer_archivo(nombre):
    archivo = open (nombre, "rt")
    datos = archivo.read();
    print (datos)