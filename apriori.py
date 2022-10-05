#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:05:55 2019

@author: juangabriel
"""

#Apriori

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)      # El header=none es para que la primera fila no la reconozca como indice
transactions = []
for i in range(0, 7501):        # hace un bucle de la fila 0 a la fila 7500
    transactions.append([str(dataset.values[i, j]) for j in range(0,20)])       # Hace un bucle de la colmna 0 a la columna 20
    
    
# Entrenar el algoritmo de Apriori
from apyori import apriori
rules = apriori(transactions, min_support = 0.003 , min_confidence = 0.2,
                min_lift = 3, min_length = 2)
# min_support = 0.003 es el numero de transacciones que contienen un item, dividido por el numero total de transacciones
# min_confidence ir probando valores
# min_lift ir probando valores
# min_length es la cantidad minima de objetos que podemos relacionar

# Visualización de los resultados
results = list(rules)

print(results[4])   # Cada numero es una relacion de comida