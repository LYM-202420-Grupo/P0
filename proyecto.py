import ply.lex as lex 
import re 
import codecs 
import os
import sys

#LISTA DE TOKENS.
tokens = ['NUMBER', 'IDENTIFIER', 'ASSIGN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'COMMA', 'PLUS', 'COLON', 'QUESTION']
 
#PALABRAS RESERVADAS.
reserved = {'exec': 'EXEC', 'new': 'NEW', 'var': 'VAR', 'macro': 'MACRO', 'if': 'IF', 'then': 'THEN', 'else': 'ELSE', 'fi': 'FI', 'do': 'DO', 'od': 'OD', 'rep': 'REP', 'times': 'TIMES',
            'turntomy': 'TURN_TO_MY', 'turntothe': 'TURN_TO_THE', 'walk': 'WALK', 'jump': 'JUMP', 'drop': 'DROP', 'pick': 'PICK', 'grab': 'GRAB', 'letgo': 'LET_GO', 'pop': 'POP', 'moves': 'MOVES',
            'nop': 'NOP', 'safeexe': 'SAFE_EXE', 'isblocked?': 'IS_BLOCKED', 'isfacing?': 'IS_FACING', 'zero?': 'ZERO', 'not': 'NOT'}

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

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = reserved.get(t.value.lower(), 'IDENTIFIER')
    t.type = t.value
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("caracter ilegal '%s" % t.value[0])
    t.lexer.skip(1)
    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
lexer = lex.lex()

data = '''
 EXEC {
 if not(blocked?(left)) then { turnToMy(left); walk(1); } else {nop;}
    fi
 }
 
 EXEC {
    safeExe(walk(1));
    moves(left,left, forward, right, back);
 }
 
 NEW VAR rotate= 3
 NEW MACRO foo (c, p)
 {  drop(c);
    letgo(p);
    walk(rotate);
}
EXEC { foo (1 ,3) }
NEW VAR one= 1
NEW MACRO goend ()
{
    if not (blocked?(front))
    then { move(one); goend(); }
    else { nop; }
    fi;
}


NEW MACRO fill ()
{
repeat roomForChips times
{ if not (zero?(myChips)) { drop(1);} else { nop; } fi ;} ;
}
NEW MACRO fill1 ()
{
while not zero?(rooomForChips)
{ if not (zero?(myChips)) { drop(1);} else { nop; } fi ;
} ;
}
NEW MACRO grabAll ()
{ grab (balloonsHere):
}
'''
    
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)