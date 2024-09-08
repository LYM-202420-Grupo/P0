import ply.lex as lex 
import re 
import os
import sys

#LISTA DE TOKENS.
tokens = ['MOVE','TURN_RIGHT' ,'DROP_CHIP' ,'PLACE_BALLOON' ,'PICKUP_CHIP' ,'GRAB_BALLOON' ,'POP_BALLOON' , 'GOTO' ,'NEW_VAR' ,'NUMBER', 'ID','EQUALS' ,'NEW_MACRO', 
          'ASSIGN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'COMMA', 'PLUS', 'COLON', 'QUESTION']
 
#PALABRAS RESERVADAS.
reserved = {'exec': 'EXEC', 'new': 'NEW', 'var': 'VAR', 'macro': 'MACRO', 'if': 'IF', 'then': 'THEN', 'else': 'ELSE', 'fi': 'FI', 'do': 'DO', 'od': 'OD', 'rep': 'REP', 'times': 'TIMES',
            'turntomy': 'TURN_TO_MY', 'turntothe': 'TURN_TO_THE', 'walk': 'WALK', 'jump': 'JUMP', 'drop': 'DROP', 'pick': 'PICK', 'grab': 'GRAB', 'letgo': 'LET_GO', 'pop': 'POP', 'moves': 'MOVES',
            'nop': 'NOP', 'safeexe': 'SAFE_EXE', 'isblocked': 'IS_BLOCKED', 'isfacing': 'IS_FACING', 'zero': 'ZERO', 'not': 'NOT'}

tokens = tokens + list(reserved.values())

t_ignore = ' \t'

#DEFINIFR EXPRESIONES REGULARES SIMPLES.
t_SEMICOLON = r';'
t_COMMA = r','
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_COLON = r':'
t_QUESTION = r'\?'

#CONDICIONES ESPECIFICAS.
t_IS_BLOCKED = r'isBlocked\?'
t_IS_FACING =  r'isFacing\?'
t_ZERO = r'zero\?'
t_NOT = r'not'

#Reconocimiento de numeros.
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Identificadores y palabras reservadas.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = reserved.get(t.value.lower(), 'ID')
    t.type = t.value
    return t

#Ignorar comentarios.
def t_COMMENT(t):
    r'\#.*'
    pass

#Manejo de lineas nuevas.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)   
    
#Manejo de errores.    
def t_error(t):
    print("caracter ilegal '%s" % t.value[0])
    t.lexer.skip(1)

#Construye el lexer. 
lexer = lex.lex()

#Esta funcion lee el archivo.
def leer_archivo(archivo):
    
    with open(archivo, 'r') as file:
        data = file.read()
        return data

#Esta funcion analiza el archivo.
def analyze_file(filename):
    
    data = leer_archivo(filename)
    lexer.input(data)
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

if __name__ == '__main__':
    archivo = 'code-examples.txt'
    if os.path.exists(archivo):
        resultado = analyze_file(archivo)
        if resultado:
            print('Si, el codigo es valido.')
        else:
            print('No, el codigo tiene errores')
    else:
        print('El archivo {0} no ha sido encontrado.'.format(archivo))
    
