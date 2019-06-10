from datetime import datetime

datahr = datetime.now()

def cabecalho():
    print('****************************************')
    print('*                                      *')
    print('* Aluno: IUDI ZURBA MELGAREJO          *')
    print('*                                      *')
    print('* Curso: ADS11                         *')
    print('*                                      *')
    print(datahr.strftime('* Data: %d/%m/%Y - %H:%M             *'))
    print('*                                      *')
    print('****************************************')
    

def troca(placa):
    n_q_sai = placa[4] # numero a ser substituido por uma letra
    l_q_entra = ""
    if n_q_sai == '0':
        l_q_entra = 'A'
    elif n_q_sai == '1':
        l_q_entra = 'B'
    elif n_q_sai == '2':
        l_q_entra = 'C'
    elif n_q_sai == '3':
        l_q_entra = 'D'
    elif n_q_sai == '4':
        l_q_entra = 'E'
    elif n_q_sai == '5':
        l_q_entra = 'F'
    elif n_q_sai == '6':
        l_q_entra = 'G'
    elif n_q_sai == '7':
        l_q_entra = 'H'
    elif n_q_sai == '8':
        l_q_entra = 'I'
    elif n_q_sai == '9':
        l_q_entra = 'J'
    placa.pop(4)
    placa.insert(4,l_q_entra)
    novaPlaca = ''.join(placa)
    novaPlaca = novaPlaca.upper()
    return novaPlaca