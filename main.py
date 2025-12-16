lista_de_compras = []
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
      arquivo.write(f"Usuário: {usuario}\n")
      arquivo.write(f"Senha: {senha}")
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
         break
      else: 
         print("Tente novamente")

