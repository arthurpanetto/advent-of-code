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


def similarity(lista_esq, lista_dir):
    lista_esq.sort()
    lista_dir.sort()
    similarity_score = 0  # Variável para acumular o resultado final

    # Para cada número da lista da esquerda
    for num_esq in lista_esq:
        count = 0  # Contador de ocorrências do número na lista direita
        
        # Contar quantas vezes o número aparece na lista da direita
        for num_dir in lista_dir:
            if num_esq == num_dir:
                count += 1
        
        # Somar o produto do número e suas ocorrências na lista da direita
        similarity_score += num_esq * count
    
    return similarity_score


# Calculando o resultado
resultado = similarity(lista_esq, lista_dir)
print("Resultado:", resultado)
