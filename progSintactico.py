import ply.lex as lex
import ply.yacc as yacc

# Define tokens, ajustando a las necesidades basadas en los ejemplos anteriores
tokens = [
    'IDENTIFICADOR', 
    'NUMERO', 
    'ASIGNACION', 
    'COMILLA', 
    'PAR_ABRE', 
    'PAR_CIERRA',
    'LLAVE_ABRE', 
    'LLAVE_CIERRA', 
    'SEMICOLON', 
    'OP_RELACIONAL', 
    'INCREMENTO',
]

# Define las palabras reservadas basándose en los ejemplos y necesidades específicas
reserved = {
    'int': 'INT',
    'str': 'STR',
    'contenido': 'CONTENIDO',
    'for': 'FOR',
    'if': 'IF',
    'else': 'ELSE',
    'fun': 'FUN'
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
t_SEMICOLON = r';'
t_OP_RELACIONAL = r'(<|>|==|=>|=<|!=)'

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

# Definiciones de las reglas de producción, ajustadas y simplificadas
def p_AR(p):
    '''AR : XC
          | ciclo_for
          | condicional_if
          | funcion'''
    
def p_XC(p):
    '''XC : IDENTIFICADOR tipo ASIGNACION expresion'''
        
def p_tipo(p):
    '''tipo : INT
            | STR'''

def p_expresion(p):
    '''expresion : NUMERO
                 | COMILLA IDENTIFICADOR COMILLA'''

def p_ciclo_for(p):
    '''ciclo_for : FOR PAR_ABRE inicializacion SEMICOLON condicion SEMICOLON incremento PAR_CIERRA LLAVE_ABRE bloque_codigo LLAVE_CIERRA'''

def p_condicional_if(p):
    '''condicional_if : IF PAR_ABRE condicion PAR_CIERRA LLAVE_ABRE bloque_codigo LLAVE_CIERRA
                      | IF PAR_ABRE condicion PAR_CIERRA LLAVE_ABRE bloque_codigo LLAVE_CIERRA ELSE LLAVE_ABRE bloque_codigo LLAVE_CIERRA'''

def p_funcion(p):
    '''funcion : FUN IDENTIFICADOR PAR_ABRE parametros PAR_CIERRA LLAVE_ABRE bloque_codigo LLAVE_CIERRA'''

# Definiciones adicionales para completar las producciones
def p_inicializacion(p):
    '''inicializacion : IDENTIFICADOR INT ASIGNACION NUMERO'''

def p_condicion(p):
    '''condicion : IDENTIFICADOR OP_RELACIONAL NUMERO
                 | IDENTIFICADOR OP_RELACIONAL IDENTIFICADOR'''

def p_incremento(p):
    '''incremento : IDENTIFICADOR INCREMENTO'''

def p_bloque_codigo(p):
    '''bloque_codigo : CONTENIDO
                     | vacio'''

def p_parametros(p):
    '''parametros : IDENTIFICADOR
                  | IDENTIFICADOR COMILLA IDENTIFICADOR COMILLA
                  | vacio'''

def p_vacio(p):
    'vacio :'
    pass

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


