from sqlalchemy.orm import sessionmaker
from models import Usuarios, engine
from models import Tarefas, engine
from sqlalchemy import select, distinct

Session = sessionmaker(bind=engine)

session = Session()

def status_escolher(escolha):
    if escolha == "1": return "PENDENTE"
    if escolha == "2": return "EM_ANDAMENTO"
    if escolha == "3": return "CONCLUIDA"
    if escolha == "4": return "CANCELADA"
    return "PENDENTE"

def inserir_usuario():
    print("\n=== Inserir Usuário ===")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    if not nome or not email:
        print("Dados inválidos")
        return

    try:
        usuario = Usuarios(
            nome=nome,
            email=email,
            senha_hash=senha
        )

        session.add(usuario)
        session.commit()
        print("Usuário criado com sucesso!")

    except Exception as e:
        session.rollback()
        print("Erro ao inserir usuário ", e)


def listar_usuario():
    try:
        usuarios = session.query(Usuarios).all()
        print("\n=== Lista de Usuários ===")
        for usuarios in usuarios:
            print(f"Id:{usuarios.id}, Nome:{usuarios.nome}, Email:{usuarios.email}, Criado em:{usuarios.criado_em}")
    except Exception as e:
        session.rollback()
        print("Nenhum usuário cadastrado ", e)




def inserir_tarefa():
    print("\n=== Inserir Tarefa ===")
    usuario_id = input("ID do usuário: ").strip()
    titulo = input("Título: ").strip()
    descricao = input("Descrição: ").strip()
    escolha = input("Digite um status: 1.Pendente, 2.Em-andamento, 3.Concluido, 4.Cancelada: ").strip()

    if not usuario_id.isdigit():
        print("ID inválido.")
        return

    status = status_escolher(escolha)

    try:
        tarefa = Tarefas(
                usuario_id= usuario_id,
                titulo= titulo,
                descricao= descricao,
                status= status
            )
        session.add(tarefa)
        session.commit()
        print("Tarefa criada com sucesso!")

    except Exception as e:
        session.rollback()
        print("Erro ao inserir tarefa:", e)


def listar_tarefas():
    try:
        tarefas = session.query(Tarefas).all()
        print("\n=== Lista de Tarefas ===")
        for tarefas in tarefas:
            print(f"Id da tarefa:{tarefas.id}, id do usuário:{tarefas.usuario_id}, Título:{tarefas.titulo}, Descrição:{tarefas.descricao}, Status:{tarefas.status}, Criado em:{tarefas.criado_em}, Concluído em:{tarefas.concluido_em}")
    except Exception as e:
        session.rollback()
        print("Nenhuma tarefa cadastrada ", e)


def atualizar_tarefas():
    print("\n=== Atualizar Tarefa ===")
    id_tarefa = input("ID da tarefa: ").strip()
    escolha = input("Digite um status: 1.Pendente, 2.Em-andamento, 3.Concluido, 4.Cancelada: ").strip()

    if not id_tarefa.isdigit():
        print("ID inválido.")
        return

    status = status_escolher(escolha)
    try:
        tarefas = session.query(Tarefas).filter_by(id=id_tarefa).one_or_none()
        tarefas.status = status
    except Exception as e:
        session.rollback()
        print("Nenhuma tarefa encontrada ", e)




def remover_tarefas():
    print("\n=== Remover Tarefa ===")
    id_tarefa = input("ID da tarefa: ").strip()

    if not id_tarefa.isdigit():
        print("ID inválido.")
        return

    try:
        tarefas = session.query(Tarefas).filter_by(id=id_tarefa).one_or_none()
        session.delete(tarefas)
        session.commit()
    except Exception as e:
        session.rollback()
        print("Nenhuma tarefa encontrada ", e)

def desafio():
    try:
        tarefas = session.query(Tarefas).filter_by(titulo="Urgente").one_or_none()
        print(f"Id da tarefa:{tarefas.id}, id do usuário:{tarefas.usuario_id}, Título:{tarefas.titulo}, Descrição:{tarefas.descricao}, Status:{tarefas.status}, Criado em:{tarefas.criado_em}, Concluído em:{tarefas.concluido_em}")
    except Exception as e:
        session.rollback()
        print("Nenhuma tarefa encontrada ", e)
    



def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Inserir Usuário")
        print("2. Inserir Tarefa")
        print("3. Listar Usuários")
        print("4. Listar Tarefas")
        print("5. Atualizar Tarefa")
        print("6. Remover Tarefa")
        print("7. Desafio")
        print("8. Sair")

        escolha = input("Escolha: ").strip()

        if escolha == "1": inserir_usuario()
        elif escolha == "2": inserir_tarefa()
        elif escolha == "3": listar_usuario()
        elif escolha == "4": listar_tarefas()
        elif escolha == "5": atualizar_tarefas()
        elif escolha == "6": remover_tarefas()
        elif escolha == "7": desafio()
        elif escolha == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


menu()