# 📚 Sistema de Gerenciamento de Livros (Python)

Projeto acadêmico desenvolvido em Python para simulação de um sistema de gerenciamento de acervo de uma livraria via terminal. O objetivo do projeto foi aplicar e consolidar conceitos fundamentais de lógica de programação e estruturas de dados dinâmicas.

---

## 📌 Funcionalidades

O sistema conta com uma estrutura de menus interativos no console que permite:

- **Cadastrar Livro:** Registra nome, autor e editora, atribuindo automaticamente um ID único incremental a partir de um valor base.
- **Consultar Livro(s):**
  - Consultar todos os livros cadastrados.
  - Consultar livro por ID específico.
  - Consultar livro(s) por Autor.
  - Retornar ao menu principal.
- **Remover Livro:** Remove um livro da base de dados através do seu ID.
- **Tratamento de Exceções & Validações:** Validação de entradas do usuário para evitar erros durante a navegação nos menus.

---

## 🛠️ Conceitos e Estruturas Utilizadas

- **Estruturas de Dados:** Manipulação de **listas de dicionários** (`lista_livros = [{...}]`).
- **Uso do `.copy()`:** Garantia de integridade de dados ao inserir cópias de dicionários na lista.
- **Modularização (Funções):** Divisão de responsabilidades em funções bem definidas (`cadastrar_livro`, `consultar_livro`, `remover_livro`).
- **Controle de Fluxo:** Laços de repetição `while` para menus contínuos e estruturas condicionais `if/elif/else`.
- **Escopo e Parâmetros:** Passagem de parâmetros e controle de ID global incremental.

---

## 🚀 Como executar na sua máquina!

### Sem instalar nada -- online:
 
1. Acesse https://www.programiz.com/python-programming/online-compiler (não precisa de cadastro)
2. Copie o conteúdo do arquivo `ex-fixacao4.py` e cole no editor.
3. Clique em **Run**.
---
 
## 🕹️ Como usar o programa
 
Ao rodar, você verá a mensagem de boas-vindas e o menu principal:
 
```
==============================
 MENU PRINCIPAL
==============================
1 - Cadastrar livro
2 - Consultar livro(s)
3 - Remover livro
4 - Sair
```
 
Digite o número da opção e pressione **Enter**.
 
| Opção | O que faz |
|-------|-----------|
| `1` | Pede nome, autor e editora e cadastra o livro com um ID automático |
| `2` | Abre o submenu de consulta (todos, por ID ou por autor) |
| `3` | Pede o ID do livro e remove da lista |
| `4` | Encerra o programa |
 
### Exemplo de teste rápido
 
1. Digite `1` e cadastre um livro (ex.: *Jogos Vorazes*, *Mistborn*, *Harry Potter*).
2. Digite `1` de novo e cadastre um segundo livro.
3. Digite `2` e depois `1` para ver todos os livros cadastrados.
4. Digite `3` e informe o ID de um livro para removê-lo.
5. Digite `4` para sair.
> ⚠️ Os livros ficam guardados apenas na memória: ao fechar o programa, os dados são perdidos.
 
---

## 👤 Autor

Feito por **Ana Laura Feltrin** • [LinkedIn](https://www.linkedin.com/in/analaurafeltrin) • [GitHub](https://github.com/analaurafeltrin)

