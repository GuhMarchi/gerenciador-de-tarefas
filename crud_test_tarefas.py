import json
import sqlite3


def conectar_banco():
    conexao = sqlite3.connect("taferas.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            feita INTEGER DEFAULT 0
            
        )
    """)
    conexao.commit()
    return conexao, cursor

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []    
    
    
tarefas = carregar_tarefas()
conexao, cursor =conectar_banco()

def adicinar_terefas():
    tarefa_do_dia = input("Digite uma tarefa do dia de hoje: ")
    tarefas.append({"nome": tarefa_do_dia, "feita": False})
    cursor.execute("INSERT INTO tarefas (nome, feita) VALUES (?, ?)", (tarefa_do_dia, 0))
    conexao.commit()
    
def listar_tarefas():
    for i, tarefa_do_dia in enumerate(tarefas):
        if tarefa_do_dia ["feita"] == True:
            print(i + 1, "✅", tarefa_do_dia["nome"])
        else:
            print(i + 1, "⬜", tarefa_do_dia["nome"])
            
def concluir_tarefa():
        listar_tarefas()
        numero = int(input("Qual terefa você concluiu? ")) - 1
        tarefas[numero]["feita"] = True
        cursor.execute("UPDATE tarefas SET feita = 1 WHERE id = ?", (numero + 1,))
        conexao.commit()
        print("Tarefa feita!")
        
def deletar_terefas():
    listar_tarefas()
    numero = int(input("Qual tarefa você quer excluir? ")) - 1
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (numero + 1,))
    conexao.commit()
    tarefas.pop(numero)
    print("tarefas deletadas")      
        
def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
         json.dump(tarefas, arquivo)       
    print("Tarefas salvas!")     
    


while True:
    print("1 - Adicionar tarefa")
    print("2 - Listar Tarefas")
    print("3 - Concluir Tarefa")
    print("4 - Deletar Tarefas")
    print("5 - Salvar Tarefas")
    print("6 - Sair")

    opcao = input("Escolha uma Opcao de 1 a 6 :")
    if opcao == "1":
        adicinar_terefas()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        deletar_terefas()
    elif opcao == "5":
        salvar_tarefas()
    elif opcao == "6":
        salvar_tarefas()
        conexao.close()
        print("saindo")
        break
    else:
        print("Opcao invalida!!!")
    
  
        
