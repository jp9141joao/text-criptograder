import os
import random

def Criptografar(Frase,Nivel):

    if Nivel == 1:
        os.system('cls')
        Frase = Frase.upper()
        Alfabeto =      'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Criptografia1 = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Criptografia2 = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'
        String = ''
        Layout = ''
        Cadeia = 'Encriptografando'

        Tam = len(Frase)

        for i in range(Tam):
            j = Alfabeto.find(Frase[i])
            String += f'{Criptografia1[j]}{Criptografia2[j]}'

        Tam = len(String)

        for i in range(Tam):
            while True:
                Crt = random.choice(Criptografia1)
                LayoutX = Layout + Crt
                Cadeia += '.'
                print(f'    {Cadeia}\n    {LayoutX}')
                os.system('cls')
                if len(Cadeia) == 19:
                    Cadeia = 'Encriptografando'
                if Crt == String[i]:
                    Layout += Crt
                    break
    
    elif Nivel == 2:
        os.system('cls')
        Frase = Frase.upper()
        Alfabeto =      'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Criptografia1 = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Criptografia2 = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'
        String = ''
        Layout = ''
        Cadeia = 'Encriptografando'

        Tam = len(Frase)

        for i in range(Tam):
            j = Alfabeto.find(Frase[i])
            String += f'{Criptografia1[j]}{Criptografia2[j]}'

        Frase = String
        String = ''
        Tam = len(Frase)

        for i in range(Tam):
            j = Alfabeto.find(Frase[i])
            String += f'{Criptografia1[j]}{Criptografia2[j]}'

        Tam = len(String)

        for i in range(Tam):
            while True:
                Crt = random.choice(Criptografia1)
                LayoutX = Layout + Crt
                Cadeia += '.'
                print(f'    {Cadeia}\n    {LayoutX}')
                os.system('cls')
                if len(Cadeia) == 19:
                    Cadeia = 'Encriptografando'
                if Crt == String[i]:
                    Layout += Crt
                    break
    
    elif Nivel == 3:
        os.system('cls')
        Frase = Frase.upper()
        Alfabeto =      'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Criptografia1 = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Criptografia2 = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'
        String = ''
        Layout = ''
        Cadeia = 'Encriptografando'

        Tam = len(Frase)

        for i in range(Tam):
            j = Alfabeto.find(Frase[i])
            String += f'{Criptografia1[j]}{Criptografia2[j]}'

        Frase = String
        String = ''
        Tam = len(Frase)

        for i in range(Tam):
            j = Alfabeto.find(Frase[i])
            String += f'{Criptografia1[j]}{Criptografia2[j]}'

        Frase = String
        String = ''
        Tam = len(Frase)

        for i in range(Tam):
            j = Alfabeto.find(Frase[i])
            String += f'{Criptografia1[j]}{Criptografia2[j]}'

        Tam = len(String)

        for i in range(Tam):
            while True:
                Crt = random.choice(Criptografia1)
                LayoutX = Layout + Crt
                Cadeia += '.'
                print(f'    {Cadeia}\n    {LayoutX}')
                os.system('cls')
                if len(Cadeia) == 19:
                    Cadeia = 'Encriptografando'
                if Crt == String[i]:
                    Layout += Crt
                    break  

    else:
        print('Opção Invalida!')
        return      

    os.system('cls')
    print(f'Mensagem Encriptografada com Sucesso!\nSua frase encriptografada é "{String}"')  

    Continuar = int(input('Deseja continuar\n1- Sim\n2- Não\nR: '))

    if Continuar == 1:
        return True
    else: 
        return False

def Descriptografar(Frase,Nivel):

    if Nivel == 1:
        Frase = Frase.upper()
        Alfabeto =      'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Criptografia1 = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Criptografia2 = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'
        String = ''
        Layout = ''
        Cadeia = 'Descriptografando'

        

        Tam = len(Frase)

        for i in range(Tam):
            if i % 2 == 0:
                j = Criptografia1.find(Frase[i])
                String += f'{Alfabeto[j]}'

        Tam = len(String)

        for i in range(Tam):
            while True:
                Crt = random.choice(Alfabeto)
                LayoutX = Layout + Crt
                Cadeia += '.'
                print(f'    {Cadeia}\n    {LayoutX}')
                os.system('cls')
                if len(Cadeia) == 19:
                    Cadeia = 'Descriptografando'
                if Crt == String[i]:
                    Layout += Crt
                    break
                
        os.system('cls')
        print(f'Mensagem Encriptografada com Sucesso!\nSua frase descriptografada é "{String}"')

    elif Nivel == 2:
        Frase = Frase.upper()
        Alfabeto =      'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Criptografia1 = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Criptografia2 = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'
        String = ''
        Layout = ''
        Cadeia = 'Descriptografando'

        Tam = len(Frase)

        for i in range(Tam):
            if i % 2 == 0:
                j = Criptografia1.find(Frase[i])
                String += f'{Alfabeto[j]}'

        Frase = String
        String = ''
        Tam = len(Frase)

        for i in range(Tam):
            if i % 2 == 0:
                j = Criptografia1.find(Frase[i])
                String += f'{Alfabeto[j]}'

        Tam = len(String)

        for i in range(Tam):
            while True:
                Crt = random.choice(Alfabeto)
                LayoutX = Layout + Crt
                Cadeia += '.'
                print(f'    {Cadeia}\n    {LayoutX}')
                os.system('cls')
                if len(Cadeia) == 19:
                    Cadeia = 'Descriptografando'
                if Crt == String[i]:
                    Layout += Crt
                    break
                
        os.system('cls')
        print(f'Mensagem Encriptografada com Sucesso!\nSua frase descriptografada é "{String}"')
    
    elif Nivel == 3:
        Frase = Frase.upper()
        Alfabeto =      'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Criptografia1 = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Criptografia2 = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'
        String = ''
        Layout = ''
        Cadeia = 'Descriptografando'

        Tam = len(Frase)

        for i in range(Tam):
            if i % 2 == 0:
                j = Criptografia1.find(Frase[i])
                String += f'{Alfabeto[j]}'

        Frase = String
        String = ''
        Tam = len(Frase)

        for i in range(Tam):
            if i % 2 == 0:
                j = Criptografia1.find(Frase[i])
                String += f'{Alfabeto[j]}'

        Frase = String
        String = ''
        Tam = len(Frase)

        for i in range(Tam):
            if i % 2 == 0:
                j = Criptografia1.find(Frase[i])
                String += f'{Alfabeto[j]}'

        Tam = len(String)

        for i in range(Tam):
            while True:
                Crt = random.choice(Alfabeto)
                LayoutX = Layout + Crt
                Cadeia += '.'
                print(f'    {Cadeia}\n    {LayoutX}')
                os.system('cls')
                if len(Cadeia) == 19:
                    Cadeia = 'Descriptografando'
                if Crt == String[i]:
                    Layout += Crt
                    break
                
        os.system('cls')
        print(f'Mensagem Encriptografada com Sucesso!\nSua frase descriptografada é "{String}"')

    else:
        print('Opção Invalida!')
        return

    Continuar = int(input('Deseja continuar\n1- Sim\n2- Não\nR: '))
    if Continuar == 1:
        return True
    else: 
        return False

while True:
    os.system('cls')
    Opcao = int(input('* Menu de Opção *\n1- Criptografar\n2- Descriptogradar\n3- Sair\nR: '))
    if Opcao == 3:
        print('Programa Encerrado!')
        break

    elif Opcao == 1:
        os.system('cls')
        Nivel = int(input('Selecione o Nivel de Criptografia:\n1- Amadora\n2- Media\n3- Militar\nR: '))
        Frase = str(input('Digite a String que deseja criptografar: '))

        if Criptografar(Frase,Nivel) == False:
            print('Programa Encerrado!')
            break

    elif Opcao == 2:
        os.system('cls')
        Nivel = int(input('Selecione o Nivel de Criptografia da frase:\n1- Amadora\n2- Media\n3- Militar\nR: '))
        Frase = str(input('Digite a String que deseja Descriptografar: '))

        Descriptografar(Frase,Nivel)

        if Descriptografar(Frase,Nivel) == False:
            print('Programa Encerrado!')
            break

    else:
        print('Opção Invalida')
