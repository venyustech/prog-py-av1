# opção um em:

# opção dois em:
# import op2_listar_contatos
gavetaDeContatos = ''

iniciarPrograma = True
while iniciarPrograma:
  print('''
  Menu
      1 - Inserir Contato\n
      2 - Listar Contatos\n
      3 - Imprimir Contato\n
      4 - Atualizar Contato\n
      5 - Remover Contato\n
      6 - Sair
  ''')

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
    while True:
      email = input("Insira o EMAIL (formato: palavra1@palavra2.palavra3): ")
      if email == "":
        print("Campo obrigatório*")
      elif email.count("@") != 1:
        print("Formato inválido. Tente novamente.")
      else:
        parte1 = email[:email.find("@")]
        resto = email[email.find("@") + 1:]
        if "." not in resto:
          print("Formato inválido. Tente novamente.")
        else:
          break
        break

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

    contato = f"[{nome}, {sobrenome}, {celular}, {telefone}, {email}, {dia_aniv},   {mes_aniv}, {ano_aniv}]"
    if gavetaDeContatos == '  ':
      gavetaDeContatos = contato
    else:
      gavetaDeContatos += ',' + contato

    print('Contato inserido com sucesso!')

  #-------------------------------------------------------------
  if (opcao == 2):
    print("Gaveta de Contatos:", gavetaDeContatos)

  continue
