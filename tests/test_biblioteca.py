import pytest
from unittest.mock import patch
from io import StringIO

# Importando as funções a serem testadas
from biblioteca import adicionar_livro, listar_livros, remover_livro, adicionar_usuario, listar_usuarios, registrar_emprestimo, livros, usuarios

@pytest.fixture
def limpar_dados():
    """Limpa os dados antes de cada teste"""
    livros.clear()
    usuarios.clear()

def test_adicionar_livro(limpar_dados):
    """Testa a adição de um livro à biblioteca"""
    with patch("builtins.input", side_effect=["O Pequeno Príncipe", "Antoine de Saint-Exupéry"]), patch("sys.stdout", new_callable=StringIO) as saida:
        adicionar_livro()
        assert len(livros) == 1
        assert livros[0]["titulo"] == "O Pequeno Príncipe"
        assert "foi adicionado com sucesso" in saida.getvalue()

def test_listar_livros_vazio(limpar_dados):
    """Testa a listagem de livros quando não há nenhum cadastrado"""
    with patch("sys.stdout", new_callable=StringIO) as saida:
        listar_livros()
        assert "Não há livros cadastrados." in saida.getvalue()

def test_remover_livro(limpar_dados):
    """Testa a remoção de um livro"""
    livros.append({"titulo": "Dom Quixote", "autor": "Cervantes", "disponivel": True})
    
    with patch("builtins.input", return_value="Dom Quixote"), patch("sys.stdout", new_callable=StringIO) as saida:
        remover_livro()
        assert len(livros) == 0
        assert "foi removido com sucesso" in saida.getvalue()

def test_remover_livro_inexistente(limpar_dados):
    """Testa a tentativa de remover um livro que não existe"""
    with patch("builtins.input", return_value="Livro Fantasma"), patch("sys.stdout", new_callable=StringIO) as saida:
        remover_livro()
        assert "Livro não encontrado." in saida.getvalue()

def test_adicionar_usuario(limpar_dados):
    """Testa a adição de um usuário"""
    with patch("builtins.input", side_effect=["João", "99999-9999", "Rua A"]), patch("sys.stdout", new_callable=StringIO) as saida:
        adicionar_usuario()
        assert len(usuarios) == 1
        assert usuarios[0]["nome"] == "João"
        assert "foi cadastrado com sucesso" in saida.getvalue()

def test_listar_usuarios_vazio(limpar_dados):
    """Testa a listagem de usuários quando não há nenhum cadastrado"""
    with patch("sys.stdout", new_callable=StringIO) as saida:
        listar_usuarios()
        assert "Não há usuários cadastrados." in saida.getvalue()

def test_registrar_emprestimo(limpar_dados):
    """Testa o empréstimo de um livro"""
    livros.append({"titulo": "1984", "autor": "George Orwell", "disponivel": True})
    usuarios.append({"nome": "Maria", "telefone": "88888-8888", "endereco": "Rua B", "livros_emprestados": []})

    with patch("builtins.input", side_effect=["Maria", "1984"]), patch("sys.stdout", new_callable=StringIO) as saida:
        registrar_emprestimo()
        assert not livros[0]["disponivel"]
        assert "foi emprestado para Maria" in saida.getvalue()

def test_registrar_emprestimo_usuario_inexistente(limpar_dados):
    """Testa o empréstimo de um livro para um usuário que não existe"""
    livros.append({"titulo": "1984", "autor": "George Orwell", "disponivel": True})

    with patch("builtins.input", side_effect=["Carlos", "1984"]), patch("sys.stdout", new_callable=StringIO) as saida:
        registrar_emprestimo()
        assert "Usuário não encontrado." in saida.getvalue()

def test_registrar_emprestimo_livro_indisponivel(limpar_dados):
    """Testa o empréstimo de um livro que já foi emprestado"""
    livros.append({"titulo": "1984", "autor": "George Orwell", "disponivel": False})
    usuarios.append({"nome": "Ana", "telefone": "77777-7777", "endereco": "Rua C", "livros_emprestados": []})

    with patch("builtins.input", side_effect=["Ana", "1984"]), patch("sys.stdout", new_callable=StringIO) as saida:
        registrar_emprestimo()
        assert "Livro não disponível para empréstimo ou não encontrado." in saida.getvalue()
