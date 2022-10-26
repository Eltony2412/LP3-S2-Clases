# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:44:03 2022

@author: user
"""

igv = 0.18

def obtenerIGVconSubtotal(Subtotal):
    return Subtotal*igv

def obtenerTotalconSubtotal(Subtotal):
    return Subtotal*(1 + igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total - obtenerSubtotalconTotal(total)