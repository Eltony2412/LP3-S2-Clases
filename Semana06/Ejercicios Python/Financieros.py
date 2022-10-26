# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:52:47 2022

@author: user
"""

import facturacion

subtotal = 800.7

print(f"subtotal:{subtotal}")
print(f"IGV: {facturacion.obtenerIGVconSubtotal(subtotal): .2f}")
print(f"TOTAL: {facturacion.obtenerTotalconSubtotal(subtotal): .2f}")