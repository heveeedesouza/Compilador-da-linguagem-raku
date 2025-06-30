import ply.lex as lex

tokens = ('NUMBER', 'WORD', 'PLUS')
states = (
    ('foo', 'exclusive'),
    ('bar', 'inclusive'),
)

t_WORD = r'[a-zA-Z]+'
t_NUMBER = r'\d+'
t_ignore = ' \t'
t_foo_ignore = ' \t'
t_foo_NUMBER = r'\d+'
t_foo_PLUS = r'\+'

def t_begin_foo(t):
    r'<foo>'
    t.lexer.begin('foo')

def t_foo_end_foo(t):
    r'</foo>'
    t.lexer.begin('INITIAL')

def t_begin_bar(t):
    r'<bar>'
    t.lexer.begin('bar')

def t_bar_end_bar(t):
    r'</bar>'
    t.lexer.begin('INITIAL')

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_foo_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print('error in INITIAL state, %s' % t.value[0])
    t.lexer.skip(1)

def t_foo_error(t):
    print('error in foo state, %s' % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input("lft muito legal <foo> 123 + 456 </foo> <bar> abc 789 </bar>")
for tok in lexer:
    print(tok.value)
