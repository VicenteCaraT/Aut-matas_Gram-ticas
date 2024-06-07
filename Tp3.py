import re

def obtener_col(simbolo_entrada):
    if re.match(r"\d+", simbolo_entrada):
        return 0
    elif simbolo_entrada == "+":
        return 1
    elif simbolo_entrada == "-":
        return 2
    elif simbolo_entrada == "%":
        return 3
    elif simbolo_entrada == "(":
        return 4
    elif simbolo_entrada == ")":
        return 5
    elif simbolo_entrada == "$":
        return 6
    else:
        return 7

def obtener_fila(no_terminal):
    if no_terminal == "E":
        return 0
    elif no_terminal == "E'":
        return 1
    elif no_terminal == "T":
        return 2
    elif no_terminal == "T'":
        return 3
    elif no_terminal == "F":
        return 4
    else:
        return 5

class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def insertar(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[-1]

    def tamano(self):
        return len(self.items)

    def contenido(self):
        return self.items

# Tabla de análisis sintáctico predictivo
tabla = [
    ["E->T E'", "", "", "", "E->T E'", "", ""],
    ["", "E'->+ T E'", "E'->- T E'", "", "", "E'->ε", "E'->ε"],
    ["T->F T'", "", "", "", "T->F T'", "", ""],
    ["", "T'->ε", "T'->ε", "T'->% F T'", "", "T'->ε", "T'->ε"],
    ["F->id", "", "", "", "F->( E )", "", ""]
]

#funcion para tokenizar la entrada del usuario
def analizar_expresion(entrada):
    expresion = re.findall(r'\d+|[()+\-%]', entrada)#caracteres permitidos
    expresion.append('$') #final de expresión
    return expresion
#función para calcular la expresión
def calcular_expresion(expresion):
    try:
        resultado = eval(expresion)
        print("Resultado:", resultado)
    except Exception as e:
        print("Error:", e)

#función para construir arbol sintáctico
def evaluar(tokens):
    p = Pila()
    p.insertar("$")
    p.insertar("E")
    salida = ""
    print("{:<45}{:<60}{:<20}".format("PILA", "ENTRADA", "SALIDA"))
    print("{:<45}{:<60}{:<20}".format(str(p.contenido()), str(tokens), str(salida)))

    while tokens:
        simbolo_entrada = tokens[0]
        cima_pila = p.inspeccionar()

        if re.match(r"\d+", simbolo_entrada) and cima_pila == "id":#se fija si en el caracter ingresante es cualquier número, y si en la cima de la pila se encuentra id, si ambas son True,reemplaza el id por el número analizado
            p.extraer()
            tokens.pop(0)
            print("{:<45}{:<60}{:<20}".format(str(p.contenido()), str(tokens), str(salida)))
        elif cima_pila == simbolo_entrada:
            if cima_pila == '$':
                print("Arbol sintáctico construido!")
                break
            else:
                p.extraer()
                tokens.pop(0)
                print("{:<45}{:<60}{:<20}".format(str(p.contenido()), str(tokens), str(salida)))
        else:
            col = obtener_col(simbolo_entrada)
            fil = obtener_fila(cima_pila)

            salida = tabla[fil][col]
            if salida != "":
                p.extraer()
                posicion = salida.find(">")
                produccion = salida[posicion+1:]
                produccion_pila = []

                for simbolo in produccion.split():
                    if simbolo != 'ε':
                        produccion_pila.append(simbolo)

                for simbolo in reversed(produccion_pila):
                    if simbolo != 'ε':
                        p.insertar(simbolo)

                print("{:<45}{:<60}{:<20}".format(str(p.contenido()), str(tokens), str(salida)))
            else:
                print("Error de sintaxis.")
                break

    if p.estaVacia() and not tokens:
        print("Expresión válida")

entrada_usuario = input("Ingrese una expresión: ")
expresion = analizar_expresion(entrada_usuario)
evaluar(expresion)
calcular_expresion(entrada_usuario)