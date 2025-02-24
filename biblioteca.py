# Gerenciamento de livros
livros = []  # Lista global para armazenar os livros
usuarios = []  # Lista global para armazenar os usuários

def adicionar_livro():
    #Adiciona um novo livro à biblioteca.
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    livros.append({"titulo": titulo, "autor": autor, "disponivel": True})
    
    print(f'O livro "{titulo}" de {autor} foi adicionado com sucesso!')


def listar_livros():
    """Lista todos os livros cadastrados na biblioteca."""
    if not livros:
        print("Não há livros cadastrados.")
        return
    
    print("\n=== Lista de Livros ===")
    for livro in livros:
        print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}')

def remover_livro():
    #Remove um livro pelo título.
    titulo_remover = input("Digite o título do livro que deseja remover: ")
    for livro in livros:
        if livro["titulo"].lower() == titulo_remover.lower():
            livros.remove(livro)
            print(f'O livro "{titulo_remover}" foi removido com sucesso!')
            return
    print("Livro não encontrado.")

# Gerenciamento de usuários
#def adicionar_usuario():
 #   #Adiciona um novo usuário à biblioteca.
  #  nome = input("Digite o nome do usuário: ")
   # usuarios.append({"nome": nome, "livros_emprestados": []})
    #print(f'O usuário "{nome}" foi cadastrado com sucesso!')
    
def adicionar_usuario():
    """Adiciona um novo usuário à biblioteca, incluindo nome, telefone e endereço."""
    nome = input("Digite o nome do usuário: ")
    telefone = input("Digite o telefone do usuário: ")
    endereco = input("Digite o endereço do usuário: ")
    
    usuarios.append({
        "nome": nome,
        "telefone": telefone,
        "endereco": endereco,
        "livros_emprestados": []
    })
    
    
    print(f'O usuário "{nome}" foi cadastrado com sucesso!')
def listar_usuarios():
    """Lista todos os usuários cadastrados na biblioteca."""
    if not usuarios:
        print("Não há usuários cadastrados.")
        return

    print("\n=== Lista de Usuários ===")
    for usuario in usuarios:
        print(f'Nome: {usuario["nome"]}, Telefone: {usuario["telefone"]}, Endereço: {usuario["endereco"]}')
        
def registrar_emprestimo():
    #Registra o empréstimo de um livro a um usuário.
    nome_usuario = input("Digite o nome do usuário: ")
    titulo_livro = input("Digite o título do livro que deseja emprestar: ")

    # Verifica se o usuário existe
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["nome"].lower() == nome_usuario.lower():
            usuario_encontrado = usuario
            break
    
    if not usuario_encontrado:
        print("Usuário não encontrado.")
        return

    # Verifica se o livro existe e está disponível
    livro_encontrado = None
    for livro in livros:
        if livro["titulo"].lower() == titulo_livro.lower() and livro["disponivel"]:
            livro_encontrado = livro
            break

    if not livro_encontrado:
        print("Livro não disponível para empréstimo ou não encontrado.")
        return

    # Registra o empréstimo
    usuario_encontrado["livros_emprestados"].append(livro_encontrado["titulo"])
    livro_encontrado["disponivel"] = False
    print(f'O livro "{livro_encontrado["titulo"]}" foi emprestado para {usuario_encontrado["nome"]}.')
    
    
def consultar_livros_emprestados_disponiveis():
    #Consulta todos os livros da biblioteca, mostrando os emprestados e disponíveis.
    if not livros:
        print("Não há livros cadastrados.")
        return
    
    print("\n=== Livros na Biblioteca ===")
    for livro in livros:
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Status: {status}')

def menu():
       #Exibe um menu interativo para o usuário.
    while True:  # Mantém o menu em loop até que o usuário escolha sair
        print("\n=== Menu Interativo ===")  
        print("1. Adicionar livro")  
        print("2. Consultar livro")  
        print("3. Remover livro")  
        print("4. Adicionar usuário") 
        print("5. Listar usuários cadastrados") 
        print("6. Registrar empréstimo de livro")  
        print("7. Consultar livros emprestados e disponíveis")  
        print("0. Sair")  
        escolha = input("Escolha uma opção: ")  

        if escolha == "1":
            adicionar_livro()
        elif escolha == "2":
            listar_livros()
        elif escolha == "3":
            remover_livro()
        elif escolha == "4":
            adicionar_usuario()
        elif escolha == "5":
             listar_usuarios()
        elif escolha == "6":    
            registrar_emprestimo()  
        elif escolha == "7":    
            consultar_livros_emprestados_disponiveis()       
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":

# Executando o menu
  menu()
