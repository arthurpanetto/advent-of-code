# Abrir o arquivo e ler as linhas
with open("day1/input.txt", "r") as arquivo:
    linhas = arquivo.readlines()  # Lê todas as linhas do arquivo

# Criar as listas
lista_esq = []  # Para os números da primeira coluna
lista_dir = []  # Para os números da segunda coluna

# Processar cada linha e separar os valores
for linha in linhas:
    esq, dir = map(int, linha.split())  # Separar os números por espaço e converter para int
    lista_esq.append(esq)  # Adicionar o valor à lista da esquerda
    lista_dir.append(dir)  # Adicionar o valor à lista da direita

def teste(lista_esq, lista_dir):
    # Ordena ambas as listas
    lista_esq.sort()
    lista_dir.sort()
    
    # Soma das diferenças absolutas
    aux = 0
    for i in range(len(lista_esq)):
        aux += abs(lista_esq[i] - lista_dir[i])
    
    return aux


# Calculando o resultado
resultado = teste(lista_esq, lista_dir)
print("Resultado:", resultado)

