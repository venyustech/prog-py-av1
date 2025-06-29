# opção um em:

# opção dois em:
# import op2_listar_contatos
contato1 = ''
contato2 = ''
contato3 = ''
contato4 = ''
contato5 = ''


iniciarPrograma = True
while iniciarPrograma:
  menu = "MENU:\n1 - Inserir Contato\n2 - Listar Contatos\n3 - Imprimir Contato\n4 - Atualizar Contato\n5 - Remover Contato\n6 - Sair"
  print(menu)

  while True:
    usuarioInput = input("Escolha uma opção: ")
    if not usuarioInput.isdigit():
      print("Opção inválida. Tente novamente.")
      continue
    opcao = int(usuarioInput)
    if opcao < 1 or opcao > 6:
      print("Opção inválida. Tente novamente.")
    else:
      break
  #-------------------------------------------------------------
  if opcao == 1:
    #Nome    CAMPO OBRIGATÓRIO
    while True:
      nome = str(input("Insira o NOME:* "))
      valid_nome = nome.strip(
      )  #Retirar os espaços para verificar se contém apenas letras
      if nome == "":
        print("Campo obrigatório*")
      elif len(nome) > 20:  #Máx. de caracteres = 20
        print("Permitido apenas 20 caracteres.")
      elif not nome.isalpha():  #Apenas letras
        print("Formato inválido. Digite apenas letras.")
      else:
        break

    #Sobrenome    CAMPO OBRIGATÓRIO
    while True:
      sobrenome = str(input("Insira o SOBRENOME:* "))
      if sobrenome == "":
        print("Campo obrigatório*")
      elif len(sobrenome) > 20:
        print("Permitido apenas 20 caracteres.")
      elif not sobrenome.isalpha():
        print("Formato inválido. Digite apenas letras.")
      else:
        break

    #Celular    CAMPO OBRIGATÓRIO
    while True:
      celular = input("Insira o CELULAR:* ")
      if celular == "":
        print("Campo obrigatório*")
      elif len(celular) > 15:
        print("Permitido apenas 15 caracteres.")
      elif not celular.isdigit():
        print("Formato inválido. Digite apenas números.")
      else:
        break

    #Telefone    CAMPO OPCIONAL
    while True:
      telefone = input("Insira o TELEFONE: ")
      if len(telefone) > 15:
        print("Permitido apenas 15 caracteres.")
      elif not telefone.isdigit():
        print("Formato inválido. Digite apenas números.")
      else:
        break

    #Email    CAMPO OBRIGATÓRIO
    email_valido = False 
    while email_valido != True: 
      email = input("Digite o EMAIL: ") 
      posicao_arroba = email.find("@") 
      posicao_ponto = email.find(".") 
      if(len(email) >= 5 and email.count("@") == 1 and email.count(".") == 1 and posicao_arroba > 0 and posicao_arroba + 1 < posicao_ponto and posicao_ponto != len(email)-1): 
        email_valido = True 
      else: 
        print("o valor não atende a especificação do campo")

    #Aniversário    CAMPO OBRIGATÓRIO
    while True:
      dia_aniv = input("Informe o DIA de ANIVERSÁRIO:* ")
      if dia_aniv == "":
        print("Campo obrigatório*")
      elif len(dia_aniv) != 2:
        print("Formato inválido. Digite 2 algarismos.")
      elif not dia_aniv.isdigit():
        print("Formato inválido. Digite apenas números.")
      else:
        break

    while True:
      mes_aniv = input("Informe o MÊS de ANIVERSÁRIO:* ")
      if mes_aniv == "":
        print("Campo obrigatório*")
      elif len(mes_aniv) != 2:
        print("Formato inválido. Digite 2 algarismos.")
      elif not mes_aniv.isdigit():
        print("Formato inválido. Digite apenas números.")
      else:
        break

    while True:
      ano_aniv = input("Informe o ANO de ANIVERSÁRIO:* ")
      if ano_aniv == "":
        print("Campo obrigatório*")
      elif len(ano_aniv) != 4:
        print("Formato inválido. Digite 4 algarismos.")
      elif not ano_aniv.isdigit():
        print("Formato inválido. Digite apenas números.")
      else:
        break

    #guarda novo contato na gaveta de contatos quando opçao 1 é escolhida
    novo_contato = f"{nome}|{sobrenome}|{celular}|{telefone}|{email}| {dia_aniv}|{mes_aniv}|{ano_aniv}"

    if contato1 == '':
      contato1 = novo_contato
      print('Contato inserido com sucesso! O que deseja fazer agora?')
    elif contato2 == '':
      contato2 = novo_contato
      print('Contato inserido com sucesso! O que deseja fazer agora?')
    elif contato3 == '':
      contato3 = novo_contato
      print('Contato inserido com sucesso! O que deseja fazer agora?')
    elif contato4 == '':
      contato4 = novo_contato
      print('Contato inserido com sucesso! O que deseja fazer agora?')
    elif contato5 == '':
      contato5 = novo_contato
      print('Contato inserido com sucesso! O que deseja fazer agora?')
    else:
      print("Não existe mais espaço na agenda.")

  #-------------------------------------------------------------
  elif opcao == 2:
    while True:
      if contato1 != '':
        separador1 = contato1.find("|")
        separador2 = contato1.find("|", separador1 + 1)
        nome = contato1[0:separador1]
        sobrenome = contato1[separador1+1 : separador2]
        print("1 -", nome, sobrenome, sep=" ")
        break
    while True:
      if contato2 != '':
        separador1 = contato2.find("|")
        separador2 = contato2.find("|", separador1 + 1)
        nome = contato2[0:separador1]
        sobrenome = contato2[separador1+1 : separador2]
        print("2 -", nome, sobrenome, sep=" ")
        break
    
    while True:
      if contato3 != '':
        separador1 = contato3.find("|")
        separador2 = contato3.find("|", separador1 + 1)
        nome = contato3[0:separador1]
        sobrenome = contato3[separador1+1 : separador2]
        print("3 -", nome, sobrenome, sep=" ")
        break

    while True:    
      if contato4 != '':
        separador1 = contato4.find("|")
        separador2 = contato4.find("|", separador1 + 1)
        nome = contato4[0:separador1]
        sobrenome = contato4[separador1+1 : separador2]
        print("4 -", nome, sobrenome, sep=" ")
        break

    while True:   
      if contato5 != '':
        separador1 = contato5.find("|")
        separador2 = contato5.find("|", separador1 + 1)
        nome = contato5[0:separador1]
        sobrenome = contato5[separador1+1 : separador2]
        print("5 -", nome, sobrenome, sep=" ")
        break
    while True:
      if contato1 == '' and contato2 == '' and contato3 == '' and contato4 == '' and contato5 == '':
        print("Não há contatos cadastrados.")
    #-------------------------------------------------------------------------------------------------
  elif opcao == 6:
    print("Programa encerrado. Saindo...")
break
    
