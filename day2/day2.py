def verificador(lista):
    diff = [lista[i + 1] - lista[i] for i in range(len(lista) - 1)] # Verifica a diferença entre o proximo numero com o numero atual
    return (all(x in range(-3, 0) for x in diff) or  # Decrescente: -3 <= x <= -1
            all(x in range(1, 4) for x in diff))     # Crescente: 1 <= x <= 3

total = 0
with open("day2/input.txt", "r") as file:
    for line in file:
        nums = [int(num) for num in line.split()]
        if verificador(nums):
            total += 1

print(total)