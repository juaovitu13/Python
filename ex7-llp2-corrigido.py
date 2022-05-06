#questão 7 registro de clientes

cliente = [['matheus', 1],['joao', 2],['maria', 3],['fulano', 4], ['jane', 5]]
conta = [[7, 456.0, 1], [789, 45.0, 2], [948, 62684.0, 2]]
while True:
    print('-'*30)
    print('--=CONTROLE=--')
    print(cliente)
    print(conta)
    print('-'*30)
    print('\nMenu de Opções:\n')
    print('1 - Cadastrar cliente.')
    print('2 - Cadastrar conta.')
    print('3 - Remover conta.')
    print('4 - Sair\n')
    op = int(input('Opção: '))

    if op == 1:#pronto
      while True:
          print('--= Cadastro de cliente =--')
          nome_cliente = input('Nome do cliente: ')
          cod_cliente = int(input('Código do cliente: '))          
          controla_codigo = False
          for i in range(len(cliente)):
              if cod_cliente == cliente[i][1]:
                  print('-'*30)
                  print('ERRO, Código já cadastrado')
                  controla_codigo = True
                  break
          if controla_codigo:
              continue
          cliente.append([nome_cliente, cod_cliente])
          break

    if op == 2:
      while True:#pronto
        print('--= Cadastro de conta =--')
        print(cliente)
        codigo_pesquisa = int(input('Código do Cliente: '))
        controla_codigo = False
        for i in range(len(cliente)):            
            if codigo_pesquisa == cliente[i][0]:
                print('\n--= Cliente encontrado!=--\n')
                num_conta = int(input('Número da conta: '))
                valor_compra = float(input('Valor da compra: '))

                conta.append([num_conta, valor_compra, codigo_pesquisa])
                controla_codigo = True
                break
        if not controla_codigo:
          print('\n--= Cliente não encontrado!=--')
          continue
        break

    if op == 3:
        print('\n--= Excluir cliente =--')
        codigo_exclusao = int(input('Cliente a excluir? '))
        valida=True
        for i in range(len(conta)):            
            if conta[i][2] == codigo_exclusao:
                print('-'*30)
                print('\nExclusão não permitida!')
                valida=False
                break
        if valida:
            for i in range(len(cliente)):
              if cliente[i][1] == codigo_exclusao:
                print('-'*30)
                print(f'\n{cliente[i][0]} --> EXCLUIDO !')
                valida=False
                del cliente[i]
                break
        if valida:
          print('\nCliente não localizado')

    if op == 4:#pronto
        print('\nFIM DO PROGRAMA...')
        break
