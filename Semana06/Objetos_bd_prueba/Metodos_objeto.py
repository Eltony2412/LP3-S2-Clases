# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 20:50:49 2022

@author: user
"""

import sqlite3

conexion = sqlite3.connect("Objetos.db")
cursor = conexion.cursor()

def listar_base():
    consulta_listar = """ SELECT*FROM OBJETOS"""
    cursor.execute(consulta_listar)
    objetos = cursor.fetchall()
    
    for objeto in objetos:
        print (objeto)
    
    conexion.commit()
    return objeto
    
def agregar_base(nombre, cantidad, estado):
    lista_objeto = [(nombre, cantidad, estado)]
    consulta_agregar = """ INSERT INTO OBJETOS (NOMBRE, CANTIDAD, ESTADO) VALUES (?,?,?)"""
    cursor.executemany(consulta_agregar, lista_objeto)
    conexion.commit()

def editar_objeto(indice, nombre, cantidad, estado):
    lista_modificar = [(nombre, cantidad, estado, indice)]
    consulta_modificar = """ UPDATE OBJETOS SET NOMBRE = ?, CANTIDAD = ?, ESTADO = ? WHERE IDOBJETO = ?"""
    cursor.executemany(consulta_modificar, lista_modificar)
    conexion.commit()

def eliminar_objeto(indice):
    consulta_eliminar = """ DELETE FROM OBJETOS WHERE IDOBJETO = ? """
    cursor.execute(consulta_eliminar, indice)
    conexion.commit()
    