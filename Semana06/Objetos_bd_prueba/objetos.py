# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 20:09:17 2022

@author: user
"""

import sqlite3

conexion = sqlite3.connect("Objetos.db")

tabla_objetos = """
                    CREATE TABLE OBJETOS(
                    IDOBJETO INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE TEXT UNIQUE,
                    CANTIDAD INTEGER,
                    ESTADO TEXT)
                """
                
cursor = conexion.cursor();
cursor.execute(tabla_objetos)
conexion.close()