usuario = None
senha = None

#Está função tem relações com as funções login_entrar e primeiro_acesso
#A função desta é organizar os protocolos de login
def login():
   while True:
      login_inicial=input("Você está acessando este aplicativo pela primeira vez? (sim/não)").strip().lower()
      if login_inicial == "sim":
         primeiro_acesso()
         break

      elif login_inicial in ("não","nao"):
         login_entrar()
         break
      else:
         print("Resposta inválida!")

#A seguinte função serve para o caso de
#o usuario estar fazendo seu primeiro acesso
def primeiro_acesso():
   usuario=input("Qual nome de usúario você deseja? ")
   senha=input("Digite a senha desejada: ")
   print(f"Seu nome de usuário é: {usuario} e sua senha é: {senha}")
   with open("login", "w", encoding="utf-8") as arquivo:
      arquivo.write(f"{usuario}\n")
      arquivo.write(senha)
   return True

#Esta função serve para os acessos 
#seguintes do usuario que ja possui conta
def login_entrar ():
   while True:
      usuário_tentativa = input("Digite seu login: ")
      senha_tentativa = input("Digite sua senha: ")
      if usuário_tentativa == usuario and senha_tentativa == senha:
         print("Login aceito")
         return True
      else: 
         print("Tente novamente")

#Essa função é pra mostrar o menu
def exibir_menu():
    print("\n===== Lista de Compras =====")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Buscar item")
    print("5. Sair")

#Essa função adiciona os elementos a lista
def adicionar_item(lista):
    item = input("Digite o nome do item a ser adicionado: ")
    lista.append(item)
    print(f"'{item}' foi adicionado à sua lista.")

#Essa função remove os elementos escolhidos
def remover_item(lista):
    if not lista:
        print("Sua lista está vazia! Não há itens para remover.")
        return
    visualizar_lista(lista)
    item_remover = input("Digite o nome do item a ser removido: ")
    if item_remover in lista:
        lista.remove(item_remover)
        print(f"'{item_remover}' foi removido da sua lista.")
    else:
        print(f"Item '{item_remover}' não encontrado na lista.")

#Essa função mostra o que tem na lista
def visualizar_lista(lista):
    if not lista:
        print("Sua lista está vazia.")
    else:
        print("\nItens na sua lista de compras:")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")

#Essa função busca algum elemento na lista
def buscar_item(lista):
   termo = input("Digite o nome do item para pesquisar: ")
   if termo in lista:
      for i, indice in enumerate(lista):
         if termo == indice:
            print(f"Item encontrado na posição: {i}")
   else:
      print("Item não encontrado.")