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