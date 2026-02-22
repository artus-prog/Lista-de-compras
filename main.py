import funçoes
lista_compras = []

while True:
   funçoes.exibir_menu()
   escolha = input("Escolha uma opção (1-5): ") 

   if escolha == '1':
      funçoes.adicionar_item(lista_compras)

   elif escolha == '2':
      funçoes.remover_item(lista_compras)

   elif escolha == '3':
      funçoes.visualizar_lista(lista_compras)

   elif escolha == '4':
      funçoes.buscar_item(lista_compras)

   elif escolha == '5':
      print("Saindo do programa... Até logo!")
      break

   else:
      print("Opção inválida. Tente novamente.")


with open("Lista de compras", "w", encoding="utf-8") as arquivo:
   arquivo.write("___Lista de compras___\n")
   for i in lista_compras:
      arquivo.write(i)