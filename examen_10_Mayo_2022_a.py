def CrearMatriz(max_i, max_j):
    # max_i -> Orden i
    # max_j -> Orden j
    matriz = [[]]
    i = 0
    j = 0
    while True:
        if i == max_i:
            j += 1
            i = 0
            if j == 5:
                break
            if j == max_j:
                break
            matriz.append([])
            continue
        if j == 5:
            break
        print("Posición ", i, " ", j)
        val = input("Mete números entre 1 e 10: ")
        try:
            val = float(val)
        except:
            print("Error")
            continue
        if val < 1 or val > 10:
            print("Error")
            continue
        matriz[j].append(val)
        i += 1
        if i == 5:
            j += 1
            i = 0
            if j == 5:
                break
            matriz.append([])
            continue

    return matriz


def menu():
    global matriz1
    global matriz2

    while True:
        print("0 - Definir")
        print("1 - Sumar diagonales")
        print("2 - Sumar matrices")
        print("3 - Visualizar")
        print("4 - Salir")
        msg = input("Escolle unha opción: ")
        try:
            num = int(msg)
            if num < 0 or num > 4:
                print("Escribe un número entre 0 e 4")
                continue
            if num == 0:
                DefinirMatrices()
            if num == 1:
                SumarDiagonales(matriz1)
                SumarDiagonales(matriz2)
            if num == 2:
                SumarMatrices(matriz1, matriz2)
            if num == 3:
                VerMatriz(matriz1)
                VerMatriz(matriz2)
            if num == 4:
                print("Bye!")
                break
        except:
            print("Introduce un valor válido")
            print(num)
            continue


matriz1 = []
matriz2 = []


def DefinirMatrices():
    global matriz1
    global matriz2
    matriz1 = DefinirMatriz("Matriz 1")
    matriz2 = DefinirMatriz("Matriz 2")
    print()


def DefinirMatriz(nombre):
    print(nombre)
    try:
        i = int(input("Rango i (max 5): "))
        j = int(input("Rango j (max 5): "))
        if i < 1 or i > 5:
            return
        if j < 1 or j > 5:
            return
        matriz = CrearMatriz(i, j)
        return matriz
    except:
        print("Error")
        return


def SumarDiagonales(matriz):
    sumPrinc = 0
    sumSec = 0
    iter = min(len(matriz), len(matriz[0]))
    for i in range(iter):
        sumPrinc += matriz[i][i]
        sumSec += matriz[i][iter-i-1]
    print("Suma diagonal principal: ", sumPrinc)
    print("Suma diagonal secundaria: ", sumSec)


def SumarMatrices(matriz_a, matriz_b):
    if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
        print("Matrices de distinto rango")
        return ValueError
    resultado = [[]]
    for i in range(len(matriz_a)):
        for j in range(len(matriz_a[0])):
            resultado[i].append(matriz_a[i][j] + matriz_b[i][j])
        if i != len(matriz_a)-1:
            resultado.append([])
    print(resultado)


def VerMatriz(matriz):
    print(matriz)


menu()
