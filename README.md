# Aplicação CRUD Flask

Este é um projeto de uma aplicação web utilizando o framework Flask. A aplicação implementa as operações CRUD (Criar, Ler, Atualizar, Excluir) para uma entidade de "Usuário".

## 🟩 Tecnologias Utilizadas

- **Python**: Linguagem de programação. 
- **Flask**: Framework web para Python.
- **SQLite**: Banco de dados para armazenar os dados da aplicação.

## 🟩 Funcionalidades

- **Cadastrar** novos usuários.
- **Listar** usuários cadastrados.
- **Editar** usuários existentes.
- **Excluir** usuários.

## 🟩 Como Executar o Projeto

Para rodar o projeto na sua máquina local, siga os passos abaixo:

### 1. Clone o Repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/rayssawho/app-crud-flask.git
```


### 2. Crie e Ative o Ambiente Virtual

Acesse o diretório do projeto:

```bash
cd app-crud-flask
```
Crie um ambiente virtual para isolar as dependências do projeto e ative o ambiente:
> Para Windows:
```bash
python -m venv venv
```
- Ativação do ambiente virtual Windows:
```bash
.\venv\Scripts\activate
```

> Para Linux/Mac:
```bash
python3 -m venv venv
```
- Ativação do ambiente virtual Linux/Mac:
```bash
source venv/bin/activate
```

### 3. Instale as Dependências
Com o ambiente virtual ativado, instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### 4. Execute a Aplicação
```bash
python app_crud.py
```
### 5. Finalizar a Aplicação
No terminal, aperte as teclas CTRL C para finalizar a aplicação.

Para desativar o ambiente virtual, digite deactivate
no terminal e pressione a tecla enter:
```bash
deactivate
```

## 🟩 Endpoints
> **POST** `/users`
- Cria um novo usuário.

**Parâmetros de entrada (JSON)**:

```json
{
  "name": "Nome do Usuário",
  "email": "email@example.com",
  "phone": "1234567890"  // Opcional
}
```
**Resposta (201 Created)**:
```json
{
  "id": 1,
  "name": "Nome do Usuário",
  "email": "email@example.com",
  "phone": "1234567890"
}
```
**Erros**:

- **400** - Se os campos name ou email estiverem ausentes.
- **500** - Se houver um erro ao salvar o novo usuário no banco de dados.

---

> **GET** `/users`
- Retorna a lista de todos os usuários cadastrados.

**Resposta (200 OK)**:

```json
[
  {
    "id": 1,
    "name": "Nome do Usuário 1",
    "email": "email1@example.com",
    "phone": "1234567890"
  },
  {
    "id": 2,
    "name": "Nome do Usuário 2",
    "email": "email2@example.com",
    "phone": "9876543210"
  }
]
```
**Erros**:

- **500** - Se houver erro ao recuperar os usuários do banco de dados.

---

> **GET** `/users/<int:id>`
- Retorna um usuário específico com base no Id fornecido.

**Parâmetros de entrada**

- id: Id do usuário (número inteiro).

**Resposta (200 OK)**:

```json
{
  "id": 1,
  "name": "Nome do Usuário",
  "email": "email@example.com",
  "phone": "1234567890"
}
```
**Erros**:

- **404** - Se o usuário com o ID fornecido não for encontrado.
- **500** - Se houver erro ao buscar o usuário no banco de dados.

---
> **PUT** `/users/<int:id>`
- Atualiza os dados de um usuário existente com base no Id.

**Parâmetros de entrada (JSON)**:

```json
{
  "name": "Novo Nome do Usuário",
  "email": "novoemail@example.com",
  "phone": "1122334455"  // Opcional
}
```
**Resposta (200 OK)**:
```json
{
  "id": 1,
  "name": "Novo Nome do Usuário",
  "email": "novoemail@example.com",
  "phone": "1122334455"
}
```

**Erros**:

- **404** - Se o usuário com o ID fornecido não for encontrado.
- **500** - Se houver erro ao atualizar os dados do usuário.

---
> **DELETE** `/users/<int:id>`
- Exclui um usuário com base no ID fornecido.

**Parâmetros de entrada**:
- id: ID do usuário (número inteiro).

**Resposta**:
```json
{
  "Info": "Usuário excluído com sucesso"
}
```

**Erros**:

- **404** - Se o usuário com o ID fornecido não for encontrado.
- **500** - Se houver erro ao excluir o usuário do banco de dados.


## 🟩 Author
[<img loading="lazy" src="https://avatars.githubusercontent.com/u/86988053?v=4" width=115><br><sub>Rayssa Alcântara Melo</sub>](https://www.linkedin.com/in/rayssarte/)