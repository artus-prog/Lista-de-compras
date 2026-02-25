import funcoes
import interface


lista_compras = []

while True:
   funcoes.exibir_menu()
   escolha = input("Escolha uma opção (1-5): ") 

   if escolha == '1':
      funcoes.adicionar_item()

   elif escolha == '2':
      funcoes.remover_item()

   elif escolha == '3':
      funcoes.visualizar_lista()

   elif escolha == '4':
      funcoes.buscar_item()

   elif escolha == '5':
      print("Saindo do programa... Até logo!")
      break

   else:
      print("Opção inválida. Tente novamente.")


with open("Lista de compras", "w", encoding="utf-8") as arquivo:
   arquivo.write("___Lista de compras___\n")
   for i in lista_compras:
      arquivo.write(i)