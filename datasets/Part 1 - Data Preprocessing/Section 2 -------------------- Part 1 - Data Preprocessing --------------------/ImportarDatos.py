
# como Importar una libreria

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importar el dataset

dataset = pd.read_csv("./Data.csv")
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values
print(Y)
