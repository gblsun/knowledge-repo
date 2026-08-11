# %% Transposta de Matriz no Python

import numpy as np
import pandas as pd

# Cria uma matriz 3x3
B = np.array([[3, 4, -1], [5, -1, 5], [4, 6, 5]])

# Calcula a transposta da matriz B
Bt = np.transpose(B)

# Converte a matriz transposta em um DataFrame para visualização
df_Bt = pd.DataFrame(Bt)

# Converte a matriz original em um DataFrame para visualização
df_B = pd.DataFrame(B)

# Imprime a matriz original e sua transposta
print(f"A transposta de \n\n{df_B}\n\né:\n\n{df_Bt}")

# %% Soma de matrizes com Python

import numpy as np
import pandas as pd

# Cria duas matrizes 3x3
A = np.array([[1, -3, 4], [3, 6, 9], [-1, 5, 4]])
B = np.array([[3, 4, -1], [5, -1, 5], [4, 6, 5]])

# Soma as duas matrizes
C = A + B
# Converte as matrizes originais em um DataFrame para visualização
df_A = pd.DataFrame(A)
df_BB = pd.DataFrame(B)

# Converte a matriz resultante da soma em um DataFrame para visualização
df_C = pd.DataFrame(C)

# Imprime a matriz resultante da soma
print(f"A soma de \n\n{df_A}\n\n + \n\n{df_BB}\n\n é igual a \n\n{df_C}")

# %%
