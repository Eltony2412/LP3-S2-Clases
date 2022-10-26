# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:59:25 2022

@author: user
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")

consulta = """INSERT INTO PAIS (NOMBRE, ESTADO) VALUES ('BRASIL', 'A') """

cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()

conexion.close()    