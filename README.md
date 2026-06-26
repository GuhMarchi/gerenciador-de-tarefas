# 📋 Gerenciador de Tarefas

Sistema de gerenciamento de tarefas desenvolvido em Python com armazenamento em SQLite e JSON. Projeto desenvolvido durante meus estudos de Análise e Desenvolvimento de Sistemas.

## 🔗 Repositório

👉 [github.com/GuhMarchi/gerenciador-de-tarefas](https://github.com/GuhMarchi/gerenciador-de-tarefas)

---

## 📌 Sobre o projeto

Sistema CRUD completo que roda no terminal, permitindo ao usuário gerenciar suas tarefas do dia a dia com persistência de dados em banco de dados SQLite e arquivo JSON.

---

## ✅ Funcionalidades

- Adicionar tarefas
- Listar tarefas com status (✅ concluída / ⬜ pendente)
- Marcar tarefa como concluída
- Deletar tarefas
- Salvar tarefas em arquivo JSON
- Persistência de dados com banco de dados SQLite

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Uso |
|------------|-----|
| Python 3 | Linguagem principal |
| SQLite3 | Banco de dados local |
| JSON | Armazenamento secundário |

---

## 📁 Estrutura do projeto

```
gerenciador-de-tarefas/
│
├── crud_test_tarefas.py   # Código principal do sistema
├── taferas.db             # Banco de dados SQLite
├── tarefas.json           # Arquivo de persistência JSON
└── README.md              # Documentação do projeto
```

---

## ▶️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/GuhMarchi/gerenciador-de-tarefas.git
```

2. Acesse a pasta:
```bash
cd gerenciador-de-tarefas
```

3. Execute o programa:
```bash
python crud_test_tarefas.py
```

---

## 🖥️ Como usar

Ao executar o programa, o menu será exibido:

```
1 - Adicionar tarefa
2 - Listar Tarefas
3 - Sair
4 - Concluir Tarefa
5 - Deletar Tarefas
6 - Salvar Tarefas
```

Digite o número da opção desejada e pressione Enter.

---

## 📚 Conceitos aplicados

- Listas e Dicionários
- Funções (`def`)
- Estruturas condicionais (`if/elif/else`)
- Loops (`while True`)
- Manipulação de arquivos JSON
- Banco de dados com SQLite3
- CRUD completo (Create, Read, Update, Delete)

---

## 👨‍💻 Autor

Desenvolvido por **Gustavo da Silva Marchi**  
Estudante de Análise e Desenvolvimento de Sistemas

[![GitHub](https://img.shields.io/badge/GitHub-GuhMarchi-181717?style=for-the-badge&logo=github)](https://github.com/GuhMarchi)

---

> Projeto desenvolvido como parte da minha jornada de aprendizado em Python e banco de dados.
