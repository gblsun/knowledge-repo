# Este trecho de código está executando a multiplicação da matriz em Python usando o Numpy.Define duas matrizes
# então cria pandas dados de dados `df_a`,` df_b` e `df_prod` para exibir as matrizes e suas
# produto de maneira formatada.
# %% Produto de Matrizes em Python

import numpy as np
import pandas as pd

A = np.array([[1, -3, 4], [3, 6, 9], [-1, 5, 4]])
B = np.array([[3, 4, -1], [5, -1, 5], [4, 6, 5]])
prod = A.dot(B)

df_A = pd.DataFrame(A)
df_B = pd.DataFrame(B)
df_prod = pd.DataFrame(prod)

print(f"O produto de \n\n{df_A}\n\nvezes\n\n{df_B}\n\né igual à:\n\n{df_prod}")

# Este trecho de código está calculando o determinante de uma matriz em Python usando a biblioteca Numpy.
# %% Cálculo de determinante no Python

import numpy as np
import pandas as pd

A2 = np.array([[1, -3, 4], [3, 6, 9], [-1, 5, 4]])
B2 = np.array([[3, 4, -1], [5, -1, 5], [4, 6, 5]])
determinante = np.linalg.det(B2)

df_A2 = pd.DataFrame(A2)
df_B2 = pd.DataFrame(B2)

print(f"A determinante de\n\n{df_B2}\n\né\n\n{determinante}")
print(determinante)
print(
    f"\n\nOu preferes assim:\n\nA determinante de\n\n{B2}\n\né\n\n{determinante}\n\n(Desta forma é sem utilizar a biblioteca pandas)"
)

# O trecho de código que você forneceu está executando a multiplicação da matriz em Python usando o Numpy.
# %% Produto de Matrizes em Python

A = np.array([[1, -3, 4], [3, 6, 9], [-1, 5, 4]])
B = np.array([[3, 4, -1], [5, -1, 5], [4, 6, 5]])
prod = A.dot(B)
print(prod)
# %% Cálculo de inversa de Matriz no Python
# teste de formatação mais organizada
import pandas as pd
import numpy as np
A3=np.array([[1,-3,4],
            [3,6,9],
            [-1,5,4]])
df_A3=pd.DataFrame(A3)
inversa =np.linalg.inv(A3)
df_inversa=pd.DataFrame(inversa)
print(f'A inversa da matriz: \n\n{df_A3}\n\n é {df_inversa}')
# %% ---end