#1
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_linha1():
    print('+ - - - -',end=' ')

def print_linha2():
    print('|        ',end=' ')

def print_linhas1():
    do_twice(print_linha1)
    print('+')

def print_linhas2():
    do_twice(print_linha2)
    print('|')

def print_figura_parcial():
    print_linhas1()
    do_four(print_linhas2)

def print_figura_total():
    do_twice(print_figura_parcial)
    print_linhas1()

print_figura_total()

