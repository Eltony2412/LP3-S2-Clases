# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:06:05 2022

@author: user
"""

import facturacion

total = 10000

print(f"Total: {total}")
print (f"Subtotal: {facturacion.obtenerSubtotalconTotal(total): .2f}")
print (f"IGV: {facturacion.obtenerIGVconTotal(total): .2f}")