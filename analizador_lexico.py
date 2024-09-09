import ply.lex as lex 
import ply.yacc as yacc
import os

#LISTA DE TOKENS.
tokens = ['MOVE','TURN_RIGHT' ,'DROP_CHIP' ,'PLACE_BALLOON' ,'PICKUP_CHIP' ,'GRAB_BALLOON' ,'POP_BALLOON' , 'GOTO' ,'NEW_VAR' ,'NUMBER', 'ID','NEW_MACRO', 
          'ASSIGN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'COMMA', 'QUESTION']
 
#PALABRAS RESERVADAS.
reserved = {'exec': 'EXEC', 'if': 'IF', 'then': 'THEN', 'else': 'ELSE', 'fi': 'FI', 'do': 'DO', 'od': 'OD', 'rep': 'REP', 'times': 'TIMES',
            'turntomy': 'TURN_TO_MY', 'turntothe': 'TURN_TO_THE', 'walk': 'WALK', 'jump': 'JUMP', 'drop': 'DROP', 'pick': 'PICK', 'grab': 'GRAB', 'letgo': 'LET_GO', 'pop': 'POP', 'moves': 'MOVES',
            'nop': 'NOP', 'safeexe': 'SAFE_EXE', 'isblocked': 'IS_BLOCKED', 'isfacing': 'IS_FACING', 'zero': 'ZERO', 'not': 'NOT', 'size': 'SIZE', 'myx': 'MYX', 'myy': 'MYY', 'mychips': 'MYCHIPS',
            'myballoons': 'MYBALLOONS', 'balloonshere': 'BALLOONSHERE', 'chipshere': 'CHIPSHERE', 'roomforchips': 'ROOMFORCHIPS'}

tokens = tokens + list(reserved.values())

#DEFINIFR EXPRESIONES REGULARES SIMPLES.
t_SEMICOLON = r';'
t_COMMA = r','
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_QUESTION = r'\?'
t_DO = r'do'
t_OD = r'od'

#Ignorar
t_ignore = ' \t'

#CONDICIONES ESPECIFICAS.
t_IS_BLOCKED = r'blocked\?'
t_IS_FACING =  r'facing\?'
t_ZERO = r'zero\?'
t_NOT = r'not'
t_DROP_CHIP = r'drop_chip'
t_GOTO = r'goto'
t_GRAB_BALLOON = r'grab_balloon'
t_NEW_MACRO = r'new_macro'
t_NEW_VAR = r'new_var'
t_PICK = r'pick'
t_PICKUP_CHIP = r'pickup_chip'
t_PLACE_BALLOON = r'place_balloon'
t_REP = r'rep'
t_TURN_RIGHT = r'turn_right'
t_TURN_TO_THE = r'turn_to_the'

#Reconocimiento de numeros.
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Identificadores y palabras reservadas.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = t.value.lower()
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        print('Error: Id descnocido {0} en la linea {1}'.format(t.value, t.lexer.lineno))
        t.type = 'ID'
            
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
    print("caracter ilegal {0}" .format(t.value[0]))
    t.lexer.skip(1)

#Construye el lexer. 
lexer = lex.lex()

# DEFINIR LAS REGLAS GRAMATICALES
def p_program_exec(p):
    '''program : EXEC block'''
    pass

def p_program_new_var(p):
    '''program : NEW_VAR ID ASSIGN NUMBER'''
    pass

def p_program_new_macro(p):
    '''program : NEW_MACRO ID LPAREN param_list RPAREN block'''
    pass

def p_block(p):
    '''block : LBRACE stmt_list RBRACE'''
    pass

def p_stmt_list(p):
    '''stmt_list : stmt SEMICOLON stmt_list
                 | stmt SEMICOLON'''
    pass

def p_stmt(p):
    '''stmt : IF condition THEN block ELSE block FI
            | WALK LPAREN NUMBER RPAREN
            | JUMP LPAREN NUMBER RPAREN
            | DROP LPAREN NUMBER RPAREN
            | MOVE LPAREN NUMBER RPAREN
            | LET_GO LPAREN NUMBER RPAREN
            | POP LPAREN NUMBER RPAREN
            | TURN_TO_MY LPAREN ID RPAREN
            | GRAB LPAREN ID RPAREN 
            | SAFE_EXE LPAREN stmt RPAREN
            | MOVES LPAREN param_list RPAREN
            | ID LPAREN param_list RPAREN
            | REP NUMBER TIMES block
            | NOP
            | TURN_RIGHT LPAREN ID RPAREN
            | TURN_TO_THE LPAREN ID RPAREN
            | PICK LPAREN ID RPAREN
            | GOTO LPAREN ID RPAREN
            | DROP_CHIP LPAREN NUMBER RPAREN
            | PLACE_BALLOON LPAREN NUMBER RPAREN
            | GRAB_BALLOON LPAREN NUMBER RPAREN
            | PICKUP_CHIP LPAREN NUMBER RPAREN
            | POP_BALLOON LPAREN NUMBER RPAREN'''
    pass

def p_stmt_do_while(p):
    '''stmt : DO block OD'''
    pass

def p_param_list(p):
    '''param_list : ID COMMA param_list
                  | ID
                  | empty'''
    pass

def p_condition(p):
    '''condition : NOT LPAREN IS_BLOCKED LPAREN ID RPAREN RPAREN
                 | NOT LPAREN ZERO QUESTION LPAREN ID RPAREN RPAREN
                 | IS_BLOCKED LPAREN ID RPAREN
                 | ZERO QUESTION LPAREN ID RPAREN
                 | IS_FACING LPAREN ID RPAREN
                 | SIZE
                 | MYX
                 | MYY 
                 | MYCHIPS
                 | MYBALLOONS
                 | BALLOONSHERE
                 | CHIPSHERE
                 | ROOMFORCHIPS'''
    pass

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}', linea {p.lineno}")
    else:
        print("Error de sintaxis al final del archivo")

# COMPILAR EL PARSER.
parser = yacc.yacc()

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
        
    result = parser.parse(data)
    
    if result is None:
        return True
    else:
        return False

#MAIN METHOD
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
    
