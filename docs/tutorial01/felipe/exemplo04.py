import ply.lex as lex

# Definindo Tokens e seus padroes
tokens = ("PLUS", "MINUS", "ID", "NUMBER", "NUMBER_FLOAT")
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_ID = r'[A-Za-z_][A-Za-z0-9_]*'
t_ignore  = ' \t'

def t_NUMBER_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    t.valeu = float(t.value)
    return t

def t_NUMBER(t):
     r'\d+'
     t.value = int(t.value)    
     return t

def t_error(t):
     print("Caractere ilegal '%s'"% t.value[0])
     t.lexer.skip(1)

def t_newline(t): #Adiciona a função t_newline
     r'\n+'
     t.lexer.lineno += len(t.value) #Atualiza o contador de linha a
                                    #depender da quantidade de \n

# Criando analisador Lexico e realizando analise lexica
lexer = lex.lex()
lexer.input("+  - --+ +  ada_ _das 10 & 13.9\nestada")
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos)