def read_line(file):
    line = file.readline()
    line = line.strip()
    return line

def read_int(file):
    line = file.readline()
    line = int(line)
    return line

def read_pair(file):
    line = file.readline()
    line = line.strip()

    list = line.split(";")

    list = [x for x in list if len(x) > 0]

    return list

def read_ints(file):
    line = file.readline()

    list = line.split(";")

    list = [int(y) for y in list if y.isdigit()]

    return list

def is_valid(path):
    file = open(path,'r')

    cadena = read_line(file)

    alfabeto = read_pair(file)

    inicio = read_int(file)

    finales = read_ints(file)

    matrix = []
    for line in file:
        func = line.split(";")
        func = [int(x) for x in func if x.isdigit()]

        matrix.append(func) 

    actual = inicio
    estado = actual
    for char in cadena:
        actual = matrix[actual][alfabeto.index(char)]
        estado = str(estado) + '/' + str(actual)

    if actual in finales:
        print("ACEPTADO")
    else:
        print("RECHAZADO")

    print(estado)
