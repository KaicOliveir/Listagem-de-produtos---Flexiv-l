lista = list()

while True:
    print('-=-' * 10)
    print('SISTEMA DE LISTAGEM DE INFORMAÇÕES')
    print('[I]nserir [E]xcluir [L]istar')
    opcao_usuario = input('Escolha uma opção: ').upper().strip()[0]
    print('-=-' * 10)

    if opcao_usuario not in 'IEL':
        print('Favor, informar um valor válido.')
        continue

    if opcao_usuario == 'I':
        try:
            valor = str(input('Digite um valor a ser inserido: '))
            lista.append(valor)
        except:
            print('Erro ao adicionar um valor na lista')
    
    elif opcao_usuario == 'E':
        try:
            valor_a_ser_excluido = input('informe o valor a ser excluido: ').strip()
            lista.remove(valor_a_ser_excluido)
            print(f'Valor {valor_a_ser_excluido} removido da lista.')
            
        except:
            print('Erro ao tentar excluir um valor da lista')
    
    elif opcao_usuario == 'L':
        try:
            if len(lista) < 1:
                print('Não tem nada para mostrar na lista.')

            for i, valor in enumerate(lista):
                print(f'{i} - {valor}')
        except:
            print('Erro ao fazer a leitura da lista')
    