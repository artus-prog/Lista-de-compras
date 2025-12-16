import funçoes
lista_compras = []

login()
while True:
   funçoes.exibir_menu()
   escolha = input("Escolha uma opção (1-4): ")     
   if escolha == '1':
      funçoes.adicionar_item(lista_compras)
   elif escolha == '2':
      funçoes.remover_item(lista_compras)
   elif escolha == '3':
      funçoes.visualizar_lista(lista_compras)
   elif escolha == '4':
      print("Saindo do programa... Até logo!")
      break
   else:
      print("Opção inválida. Tente novamente.")