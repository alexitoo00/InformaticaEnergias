def CrearMatriz(max_i, max_j):
    # max_i -> Orden i
    # max_j -> Orden j
    matriz = [[]]
    i = 0
    j = 0
    while True:
        if i == max_i:                              # Si se chega ao final da columna
            j += 1                                  # - Pásase á siguiente
            i = 0                                   # - Reiníciase o iterador de filas
            if j == max_j:                          # Si se chega á última columna
                break                               # - Terminamos a función
            matriz.append([])                       # Añadimos unha nova columna

        print("Posición [", i, " ", j, "]")         # Pedimos un valor
        val = input("Mete un valor entre 1 e 10: ")

        try:                                        # Checkeamos si é un float
            val = float(val)
        except:
            print("Error")
            continue

        if val < 1 or val > 10:                     # Comprobamos que estea entre 1 e 10
            print("Error")
            continue

        matriz[j].append(val)                       # Añadimos o valor á columna correspondiente
        i += 1

    return matriz                                   # Devolvemos o objeto matriz


def menu():
    global matriz1
    global matriz2

    while True:                                     # Definir lista de opcións
        print("0 - Definir matrices")
        print("1 - Sumar diagonales principales")
        print("2 - Sumar matrices")
        print("3 - Visualizar matrices")
        print("4 - Salir")
        msg = input("Escolle unha opción: ")
        try:                                        # Comprobar que se introducise un número de opción válido
            num = int(msg)
            if num < 0 or num > 4:
                print("Escribe un número entre 0 e 4")
                continue
            if num == 0:                            # Opción 0
                DefinirMatrices()
            if num == 1:                            # Opción 1
                SumarDiagonales(matriz1)
                SumarDiagonales(matriz2)
            if num == 2:                            # Opción 2
                SumarMatrices(matriz1, matriz2)
            if num == 3:                            # Opción 3
                VerMatriz(matriz1)
                VerMatriz(matriz2)
            if num == 4:                            # Opción 4
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
    matriz1 = DefinirMatriz("Matriz 1")             # A efectos meramente organizativos
    matriz2 = DefinirMatriz("Matriz 2")
    print()


def DefinirMatriz(nombre):
    print(nombre)
    try:
        i = int(input("Rango i (max 5): "))         # Pídese o rango da matriz (filas e columnas)
        j = int(input("Rango j (max 5): "))
        if i < 1 or i > 5:                          # Compróbase que estean entre 1 e 5
            return
        if j < 1 or j > 5:
            return
        matriz = CrearMatriz(i, j)                  # Créase a matriz có rango solicitado
        return matriz
    except:
        print("Error")
        return


def SumarDiagonales(matriz):
    sumPrinc = 0
    sumSec = 0
    iter = min(len(matriz), len(matriz[0]))         # Calculamos o valor mínimo entre filas e columnas
    for i in range(iter):
        sumPrinc += matriz[i][i]                    # Diagonal principal
        sumSec += matriz[i][iter-i-1]               # Diagonal secundaria
    print("Suma diagonal principal: ", sumPrinc)
    print("Suma diagonal secundaria: ", sumSec)


def SumarMatrices(matriz_a, matriz_b):
    if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
        print("Matrices de distinto rango")         # Compróbase que ambas matrices teñan o mismo número
        return ValueError                           #  de filas e de columnas
    
    resultado = []
    for i in range(len(matriz_a)):
        resultado.append([])                        # Añade unha columna de cada vez iterando por todas as columnas
        for j in range(len(matriz_a[0])):           # Itera por todas as filas
            resultado[i].append(matriz_a[i][j] + matriz_b[i][j])
    print(resultado)


def VerMatriz(matriz):
    print(matriz)


menu()                                              # Inicio do programa
