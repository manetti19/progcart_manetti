print("teste")

import numpy as np
lista = [1, 2, 3, 4, 5]
print(lista)
array = np.array(lista)
print(array)
print(array * 2) #legal
media = np.mean(array)
print(media)
matriz = np.random.rand(3,3,3) #gera uma matriz 3x3x3 de números aleatórios entre 0 e 1
print(matriz)
mediadamatriz = np.mean(matriz)
print(mediadamatriz)
aluno = ["joao", "maria", "pedro"]
aluno[0] = {"matematica": 10, "fisica": 9, "quimica": 7}
print(aluno[0])
aluno[1] = {"matematica": 8, "fisica": 7, "quimica": 9}
print(aluno[1])
aluno[2] = {"matematica": 9, "fisica": 8, "quimica": 10}
print(aluno[2])
