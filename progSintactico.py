import ply.lex as lex
import ply.yacc as yacc

# Define tokens
tokens = [
    'IDENTIFICADOR', 
    'NUMERO', 
    'ASIGNACION', 
    'COMILLA', 
    'PAR_ABRE', 
    'PAR_CIERRA',
    'LLAVE_ABRE', 
    'LLAVE_CIERRA', 
    'PUNTOCOMA', 
    'OP_RELACIONAL', 
    'INCREMENTO',
]

# Palabras reservadas
reserved = {
    'int': 'INT',
    'str': 'STR',
    'contenido': 'CONTENIDO',
    'for': 'FOR',
    'if': 'IF',
    'else': 'ELSE',
    'fun': 'FUN',
    'imprimir' : 'IMPRIMIR'
}

# Lista para recolectar errores
errores = []

tokens += list(reserved.values())

# Expresiones regulares
t_ASIGNACION = r'/='
t_COMILLA = r'"'
t_INCREMENTO = r'\++'
t_PAR_ABRE = r'\('
t_PAR_CIERRA = r'\)'
t_LLAVE_ABRE = r'\{'
t_LLAVE_CIERRA = r'\}'
t_PUNTOCOMA = r';'
t_OP_RELACIONAL = r'(==|=>|=<|!=|<|>)'

# Identificador o palabras reservadas
def t_IDENTIFICADOR(t):
    r'[A-Za-z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFICADOR')
    return t

# Número
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    mensaje_error = f"Carácter no permitido '{t.value[0]}'"
    errores.append(mensaje_error)
    t.lexer.skip(1)

lexer = lex.lex()

# Definiciones de las reglas 
def p_AR(p):
    '''AR :  varint
          |  varstr
          |  funcion
          |  funcionVarStr
          |  funcionVarInt
          |  ciclo_for
          |  ciclo_forImprimir
          |  ifelseImprimir
          |  ifelseImprimirInt
          |  if'''
    
#  Declaración de variables
#  a int /= 10 | Saludo str /= "Hola"
#def p_XC(p):
 #   '''XC   : IDENTIFICADOR tipoStr ASIGNACION expresionStr'''
    
def p_varint(p):
    '''varint : IDENTIFICADOR INT ASIGNACION NUMERO'''
    global nombreVarInt
    global tipoVarInt
    global valorInt

    nombreVarInt = p[1]
    tipoVarInt = p[2]
    valorInt = p[4]

    if isinstance(valorInt, int) and tipoVarInt == "int":
        print(f'variable declarada int {nombreVarInt}')
    else:
        print('Erro declaración variable, no es int')

def p_varintAux(p):
    '''varintAux : IDENTIFICADOR INT ASIGNACION NUMERO'''
    global nombreVarIntAux
    global tipoVarIntAux
    global valorIntAux

    nombreVarIntAux = p[1]
    tipoVarIntAux = p[2]
    valorIntAux = p[4]

    if isinstance(valorIntAux, int) and tipoVarIntAux == "int":
        print(f'variable declarada int {nombreVarIntAux}')
    else:
        print('Erro declaración variable, no es int')


def p_varstr(p):
    '''varstr : IDENTIFICADOR STR ASIGNACION COMILLA IDENTIFICADOR COMILLA'''
    global nombreVarStr
    global tipoVarStr
    global valorStr

    nombreVarStr = p[1]
    tipoVarStr = p[2]
    valorStr = p[5]

    if isinstance(valorStr, str) and tipoVarStr == "str":
        print(f'variable declarada str {nombreVarStr}')
    else:
        print('Erro declaración variable, no es str')

def p_varstrAux(p):
    '''varstrAux : IDENTIFICADOR STR ASIGNACION COMILLA IDENTIFICADOR COMILLA'''
    global nombreVarStrAux
    global tipoVarStrAux
    global valorStrAux

    nombreVarStrAux = p[1]
    tipoVarStrAux = p[2]
    valorStrAux = p[5]

    if isinstance(valorStrAux, str) and tipoVarStrAux == "str":
        print(f'variable declarada str {nombreVarStrAux}')
    else:
        print('Erro declaración variable, no es str')




def p_funcion(p):
    '''funcion : FUN IDENTIFICADOR PAR_ABRE PAR_CIERRA LLAVE_ABRE IMPRIMIR PAR_ABRE COMILLA IDENTIFICADOR COMILLA PAR_CIERRA LLAVE_CIERRA'''
    print(f'impresion fun: {p[9]}')

def p_funcionVarStr(p):
    '''funcionVarStr : FUN IDENTIFICADOR PAR_ABRE PAR_CIERRA LLAVE_ABRE varstr IMPRIMIR PAR_ABRE IDENTIFICADOR PAR_CIERRA LLAVE_CIERRA'''

    valorPrinStr = p[9]

    if nombreVarStr == valorPrinStr:
        print(f'{valorStr}')
    else:
        print(f'Erro variable no declarada')

def p_funcionVarInt(p):
    '''funcionVarInt : varint FUN IDENTIFICADOR PAR_ABRE IDENTIFICADOR INT PAR_CIERRA LLAVE_ABRE IMPRIMIR PAR_ABRE IDENTIFICADOR PAR_CIERRA LLAVE_CIERRA'''

    parametriId = p[5]
    parametroImprimir = p[11]

    if nombreVarInt == parametriId == parametroImprimir:
        print(f'el valor del parametro{nombreVarInt} es {valorInt}')
    else:
        print('Error parametro incorrecto')


def p_ciclo_for(p):
    '''ciclo_for : FOR PAR_ABRE varint PUNTOCOMA IDENTIFICADOR OP_RELACIONAL NUMERO PUNTOCOMA IDENTIFICADOR INCREMENTO PAR_CIERRA LLAVE_ABRE LLAVE_CIERRA'''

def p_ciclo_forImprimir(p):
    '''ciclo_forImprimir : FOR PAR_ABRE varint PUNTOCOMA IDENTIFICADOR OP_RELACIONAL NUMERO PUNTOCOMA IDENTIFICADOR INCREMENTO PAR_CIERRA LLAVE_ABRE IMPRIMIR PAR_ABRE IDENTIFICADOR PAR_CIERRA LLAVE_CIERRA'''

    idOpRelacion = p[5]
    operador = p[6]
    numero = p[7]
    idIncremento = p[9]
    imprimir = p[15]

    tabla_operadores = {
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '==': lambda x, y: x == y,
        '=<': lambda x, y: x <= y,
        '=>': lambda x, y: x >= y,
        '!=': lambda x, y: x != y,
    }

    print(F'{operador}, {numero}')

    if idOpRelacion == idIncremento == imprimir == nombreVarInt:
        valorFor = valorInt
        condicion = tabla_operadores[operador](valorFor, numero)
        
        while condicion : 
            print(valorFor)
            valorFor += 1
           
            condicion = tabla_operadores[operador](valorFor, numero)

        # for valorFor in range (condicion):
        #     print(valorFor)
    else:
        print('Error for')



def p_if(p):
    '''if : IF PAR_ABRE PAR_CIERRA LLAVE_ABRE LLAVE_CIERRA ELSE LLAVE_ABRE LLAVE_CIERRA'''


def p_ifelseImprimir(p):
    '''ifelseImprimir : varstr varstrAux IF PAR_ABRE IDENTIFICADOR OP_RELACIONAL IDENTIFICADOR PAR_CIERRA LLAVE_ABRE IMPRIMIR PAR_ABRE COMILLA IDENTIFICADOR COMILLA PAR_CIERRA LLAVE_CIERRA ELSE LLAVE_ABRE IMPRIMIR PAR_ABRE COMILLA IDENTIFICADOR COMILLA PAR_CIERRA LLAVE_CIERRA'''

    idCondicion = p[5]
    operador = p[6]
    idcondicion2 = p[7]

    tabla_operadores = {
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '==': lambda x, y: x == y,
        '=<': lambda x, y: x <= y,
        '=>': lambda x, y: x >= y,
        '!=': lambda x, y: x != y,
    }

    if idCondicion == nombreVarStr and idcondicion2 ==  nombreVarStrAux:
        condicion = tabla_operadores[operador](valorStr, valorStrAux)
        if condicion :
            print(p[13])
        else:
            print(p[22])
    else:
        print('Las variable no coinciden')

def p_ifelseImprimirInt(p):
    '''ifelseImprimirInt : varint varintAux IF PAR_ABRE IDENTIFICADOR OP_RELACIONAL IDENTIFICADOR PAR_CIERRA LLAVE_ABRE IMPRIMIR PAR_ABRE COMILLA IDENTIFICADOR COMILLA PAR_CIERRA LLAVE_CIERRA ELSE LLAVE_ABRE IMPRIMIR PAR_ABRE COMILLA IDENTIFICADOR COMILLA PAR_CIERRA LLAVE_CIERRA'''

    idCondicion = p[5]
    operador = p[6]
    idcondicion2 = p[7]

    tabla_operadores = {
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '==': lambda x, y: x == y,
        '=<': lambda x, y: x <= y,
        '=>': lambda x, y: x >= y,
        '!=': lambda x, y: x != y,
    }

    if idCondicion == nombreVarInt and idcondicion2 ==  nombreVarIntAux:
        condicion = tabla_operadores[operador](valorInt, valorIntAux)
        if condicion :
            print(p[13])
        else:
            print(p[22])
    else:
        print('Las variable no coinciden')
    
    
        
    



    


      


# #for (D int /= 0; a =< 10; Foco++){david int /= 20}
# #for (david int /= 2; pera < uva; gato++) {david int /= 20}
# #for  (         a int /= 0      ;       a => 5 | a  ;         a++        )         {           pendiente         }        
# #FOR PAR_ABRE inicializacion SEMICOLON condicion SEMICOLON incremento PAR_CIERRA LLAVE_ABRE bloque_codigo LLAVE_CIERRA
# def p_ciclo_for(p):
#     '''ciclo_for : FOR PAR_ABRE inicializacion SEMICOLON condicion SEMICOLON incremento PAR_CIERRA LLAVE_ABRE bloque_codigo LLAVE_CIERRA'''

# def p_condicional_if(p):
#     '''condicional_if : IF PAR_ABRE condicion PAR_CIERRA LLAVE_ABRE bloque_codigo LLAVE_CIERRA
#                       | IF PAR_ABRE condicion PAR_CIERRA LLAVE_ABRE bloque_codigo LLAVE_CIERRA ELSE LLAVE_ABRE bloque_codigo LLAVE_CIERRA'''

# def p_funcion(p):
#     '''funcion : FUN IDENTIFICADOR PAR_ABRE parametros PAR_CIERRA LLAVE_ABRE bloque_codigo LLAVE_CIERRA'''

# # Definiciones adicionales para completar las producciones
# def p_inicializacion(p):
#     '''inicializacion : IDENTIFICADOR INT ASIGNACION NUMERO'''

# def p_condicion(p):
#     '''condicion : IDENTIFICADOR OP_RELACIONAL NUMERO
#                  | IDENTIFICADOR OP_RELACIONAL IDENTIFICADOR'''

# def p_incremento(p):
#     '''incremento : IDENTIFICADOR INCREMENTO'''

# def p_bloque_codigo(p):
#     '''bloque_codigo : XC
#                      | condicional_if
#                      | ciclo_for
#                      | vacio'''

# def p_parametros(p):
#     '''parametros : IDENTIFICADOR
#                   | IDENTIFICADOR COMILLA IDENTIFICADOR COMILLA
#                   | vacio'''

# def p_vacio(p):
#     'vacio :'
#     pass

# Manejo de errores en el parser
def p_error(p):
    if p:
        errores.append(f"Error de sintaxis en '{p.value}'")
    else:
        errores.append("Error de sintaxis al final de la entrada")

parser = yacc.yacc()


def analizar(texto):
    errores.clear()  
    lexer.input(texto)
    tokens_list = []
    for token in lexer:
        tokens_list.append((token.type, token.value))
    parser.parse(texto)
    return errores, tokens_list


