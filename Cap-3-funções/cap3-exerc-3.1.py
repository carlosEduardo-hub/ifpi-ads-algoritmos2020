def main():
    palavra = input('palavra: ')
    right_justify(palavra)

def right_justify(s):
    tamanho_palavra = len(s)
    qtd_espaços = 70 - tamanho_palavra
    espaços = qtd_espaços * ' '
    resultado = espaços + s
    print(resultado)

main()
