# operation_selector
# José Carlos Gutiérrez Zúñiga
# Daniel Mena Brenes

# Submodulo que toma los valores verificados para realizar las operaciones.
def operacion(num1, num2, op):  # num1 y num2 son int y op es un str válido
    match op:  # "switch case" para ejecutar la opecación seleccionada
        case "+":
            return num1 + num2  # Devuelve la suma de num1 y num2
        case "-":
            return num1 - num2  # Devuelve la resta de num1 y num2
        case "*":
            return num1 * num2  # Devuelve la multiplicación de num1 y num2
        case "&":
            return num1 & num2  # Devuelve and lógico de num1 y num2


# Principal
# Entrada de datos que se esperan sean num1 y num2 sea int y op str
# La salida es de la forma código de error, resultado
def operation_selector(num1, num2, op):
    # Filtra el caso de booleanos
    if isinstance(num1, bool) or isinstance(num2, bool):
        return -50, None  # Devuelve código de error -50 y None como resultado

    if not isinstance(num1, int):  # Confirma que num1 sea int
        return -50, None  # Devuelve código de error -50 y None como resultado

    if not isinstance(num2, int):  # Confirma que num2 sea int
        return -50, None  # Devuelve código de error -50 y None como resultado

    if not isinstance(op, str):  # Confirma que op sea str
        return -60, None  # Devuelve código de error -60 y None como resultado

# Confirma que op sea un str válido
    if op == "+" or op == "-" or op == "*" or op == "&":
        return 0, operacion(num1, num2, op)  # Devuelve error 0 y el resultado

    else:
        return -70, None  # Devuelve código de error -70 y None como resultado


# Calcula el valor promedio de la lista ingresada. Max 10 elementos
# Entrada lista_valores: Una lista de números int or float.
# Salida código de error y valor promedio o None
def calculo_promedio(lista_valores):
    # Se verifica que el largo de la listo no exceda 10 elementos
    if len(lista_valores) > 10:
        return -90, None

    # Se explora los elemetos de la lista
    for i in range(len(lista_valores)):
        # Se asigna el valor de la lista a var numero
        numero = lista_valores[i]

        # Se verifica que numero no sea int o float y retorna error -90, None
        if not isinstance(numero, int):
            if not isinstance(numero, float):
                return -80, None
        if isinstance(numero, bool):
            return -80, None

    # Se retorna 0 de error y el valor promedio
    return 0, sum(lista_valores) / len(lista_valores)
