# Gerador de CPF

# Esse while é para que possa verificar varios numeros sem precisar executar novamente
while True:
    cpf = list(input('Digite o CPF: ')) #colocar as informações em uma lista
    cpf_string = ''.join(cpf) # transformar em string os valores digitados 

    # Verificar se o numero digitado tem 11 digitos
    if not (len(cpf_string) == 11):
        print("Por Favor digite um numero de 11 digitos")
    else: 
        # Esse try é para descobrir eventuais erros, por exemplo digitar uma letra, assim ele vai pro except e nao apresenta o erro, e sim uma msg estilizada
        try:
            digito1 = int(cpf_string[0])
            digito2 = int(cpf_string[1])
            digito3 = int(cpf_string[2])
            digito4 = int(cpf_string[3])
            digito5 = int(cpf_string[4])
            digito6 = int(cpf_string[5])
            digito7 = int(cpf_string[6])
            digito8 = int(cpf_string[7])
            digito9 = int(cpf_string[8])
            digito10 = int(cpf_string[9])
            digito11 = int(cpf_string[10])

            peso_digito = 10
            soma_nove_primeiros_digitos = 0
            digito_multiplicado = 0
 
            for i in range(9):
               
                digito_multiplicado = int(cpf_string[i]) * peso_digito
                soma_nove_primeiros_digitos += digito_multiplicado
                peso_digito -= 1
            resto_primeiro_digito = (soma_nove_primeiros_digitos * 10) % 11

            peso_digito = 11
            soma_dez_primeiros_digitos = 0
            digito_multiplicado = 0
 
            for i in range(10):
               
                digito_multiplicado = int(cpf_string[i]) * peso_digito
                soma_dez_primeiros_digitos += digito_multiplicado
                peso_digito -= 1
            resto_segundo_digito = (soma_dez_primeiros_digitos * 10) % 11



            # Verificação se os numeros são iguais exemplo 11111111111
            if digito1 == digito2 and digito2 == digito3 and digito3 == digito4 and digito4 == digito5 and digito5 == digito6 and digito6 == digito7 and digito7 == digito8 and digito8 == digito9 and digito9 == digito10 and digito10 == digito1:
                print("CPF INVALIDO")
            elif resto_primeiro_digito == int(cpf_string[9]) and resto_segundo_digito == int(cpf_string[10]):
                print("CPF VALIDO")
                if digito9 == 0:
                    print('CPF origem Rio Grande do Sul')
                elif digito9 == 1:
                    print(
                        'CPF origem Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul ou Tocantins')
                elif digito9 == 2:
                    print('CPF origem Amazonas, Pará, Roraima, Amapá, Acre ou Rondônia')
                elif digito9 == 3:
                    print('CPF origem Ceará, Maranhão ou Piauí')
                elif digito9 == 4:
                    print(
                        'CPF origem Paraíba, Pernambuco, Alagoas ou Rio Grande do Norte')
                elif digito9 == 5:
                    print('CPF origem Bahia e Sergipe')
                elif digito9 == 6:
                    print('CPF origem Minas Gerais')
                elif digito9 == 7:
                    print('CPF origem Rio de Janeiro ou Espírito Santo')
                elif digito9 == 8:
                    print('CPF origem São Paulo')
                elif digito9 == 9:
                    print('CPF origem Paraná ou Santa Catarina')
            else:
                print("CPF INVALIDO")
        except:
            print("CPF DEVE CONTER SOMENTE NUMEROS")

    # condicao para sair ou não do While
    add = input('Deseja Verificar mais CPF: digite [s] se sim')

    if add == 's':
        continue
    else:
        print('Finalizado com Sucesso!!')
        break
