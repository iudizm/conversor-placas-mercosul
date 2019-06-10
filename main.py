from funcs import *

print(cabecalho())
print("***** CONVERSOR DE PLACAS DO MERCOSUL *****")
print("\nDigite 'fim' para finalizar a conversão e exibir o resultado")
antigasPlacas=[]
novasPlacas=[]
cont = 0
x=False

while x == False:
    placa_antiga=input('\n--- DIGITE UMA PLACA ---\nSeguindo o formato antigo ( LLLNNNN )\nR:')
    placa_antiga=placa_antiga.upper()
    
    if placa_antiga == 'FIM':
        print('\n',cont,'placas foram atualizadas para o novo modelo MERCOSUL.')
        print('************************************************************\nPLACAS ANTIGAS:',antigasPlacas,'\nPLACAS NOVAS  :',novasPlacas)
        x = True
    else:
        antigasPlacas.append(placa_antiga) # placa antiga --> guarda
        placa=list((placa_antiga)) # lista a placa
        novaPlaca = troca(placa) # converte a placa
        novasPlacas.append(novaPlaca) # placa nova --> guarda
        cont += 1
        print("\nDigite 'fim' para finalizar a conversão e exibir o resultado")
        