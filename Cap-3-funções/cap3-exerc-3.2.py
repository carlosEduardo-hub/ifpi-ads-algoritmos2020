#1
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)

#2
def do_twice2(funcao, valor):
    funcao(valor)
    funcao(valor)

def print_spam2(palavra):
    print(palavra)

do_twice2(print_spam2,'spam')

#3
def print_twice(bruce):
    print(bruce)
    print(bruce)

#4
do_twice2(print_twice, 'spam')

#5
def do_four(funcao, valor):
    funcao(valor)
    funcao(valor)

def chamar_nome(nome):
    print(f'olá {nome}')
    print(f'olá {nome}')

do_four(chamar_nome, 'Carlos')

