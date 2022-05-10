# -*- coding: utf-8 -*-
"""
Created on Tue May 10 08:47:36 2022

@author: Alumno
"""

contar=input("Ingrese el # al que debo contar: ")
contar=int(contar)
contador=1
while True:
    print(contador)
    contador+=1
    if contador>contar:
        break
    