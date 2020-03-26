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

    subcadenas = [cadena[i: j] for i in range(len(cadena)) 
          for j in range(i + 1, len(cadena) + 1)]

    resultado = []
    for item in subcadenas:
        actual = inicio
        for char in item:
            actual = matrix[actual][alfabeto.index(char)]

        if actual in finales:
            resultado.append(item)

    resultado = list(dict.fromkeys(resultado))
    print(resultado)
