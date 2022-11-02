# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:05:58 2022

@author: UNTELS
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

cursor = conexion.cursor()

lista_autores = [('Floar Cerdan', '25/10/1978') , ('Daniel Levano', '17/01/1980'),
                 ('Omar Peña', '15/07/1984'), ('Cesar Zapata', '15/10/1960')]

lista_editoriales = [('EIU', 'A'), ('MACRO', 'A'), ('BOSCH', 'A'), ('LIMA SUR', 'A'), 
                     ('PIRAMIDE', 'A'), ('COLUMBUS', 'A'), ('CENTRO', 'A')]

lista_paises = [('PERU', 'A'), ('ARGENTINA', 'A'), ('COLOMBIA', 'A'), ('VENEZUELA', 'A'),
               ('URUGUAY', 'A'), ('PARAGUAY', 'A'), ('USA', 'A')]

lista_libros = [('Oracle 11g', 10, 2019, 50, 'A', 1, 1, 1), 
                ('SISTEMAS OPERATIVOS', 14, 2016, 59, 'A', 1, 4, 3),
                ('ESTRUCTURAS DE DATOS', 16, 2018, 20, 'A', 2, 2, 3),
                ('ALGORITMOS DE PYTHON', 18, 2017, 70, 'A', 2, 2, 1),
                ('BI', 6, 2019, 50, 'A', 1, 4, 2),
                ("INGENIERIA DE SOFTWARE", 9, 2020, 56, 'A', 3, 2, 4),
                ('ORGANIZACION DE PCS', 9, 2016, 60, 'A', 7, 2, 1),
                ('ENSAMBLAJE', 9, 2018, 50, 'A', 4, 4, 3)]

consulta_pais = """
                    INSERT INTO PAIS (NOMBRE, ESTADO) VALUES (?,?)
                """
                
consulta_editorial = """
                    INSERT INTO EDITORIAL (NOMBRE, ESTADO) VALUES (?,?)
                """ 
                
consulta_autor = """
                    INSERT INTO AUTOR (NOMBRE, F_NACIMIENTO) VALUES (?,?)
                """    
                
consulta_libro = """
                    INSERT INTO LIBRO (TITULO, CANTIDAD, ANIO, PRECIO, ESTADO, IDPAIS, IDEDITORIAL, IDAUTOR) 
                    VALUES (?,?, ?, ?, ?, ?, ?, ?)
                """          
                
cursor.executemany(consulta_pais, lista_paises)
cursor.executemany(consulta_editorial, lista_editoriales)
cursor.executemany(consulta_autor, lista_autores)
cursor.executemany(consulta_libro, lista_libros)

conexion.commit()
conexion.close()