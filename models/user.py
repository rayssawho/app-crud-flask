"""
Código com a Classe User e seus atributos, 
assim como os métodos para manipulação dos dados no banco SQLite.

"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    Representa o modelo de um Usuário no banco de dados.

    Atributos:
        id (int): Identificador único do usuário. Chave primária.
        name (str): Nome do usuário. Campo obrigatório, máximo de 100 caracteres.
        phone (int, opcional): Número de telefone do usuário. Pode ser None.
        email (str): Endereço de email do usuário. Deve ser único e é obrigatório.

    Métodos:
        __init__(self, name, email, phone=None):
            Inicializa uma instância da classe User.

        save(self):
            Salva o usuário no banco de dados.

        get_all_users() -> list[User]:
            Retorna todos os usuários armazenados no banco de dados.

        get_user_by_id(user_id: int) -> User | None:
            Retorna o usuário com base no ID fornecido. Retorna None se não encontrado.

        update(self, name: str, phone: int | None, email: str):
            Atualiza os dados do usuário no banco de dados.

        delete(self):
            Exclui o usuário do banco de dados.

        to_dict(self) -> dict:
            Converte o usuário em um dicionário para facilitar a serialização e manipulação.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name, email, phone=None):
        self.name = name
        self.email = email
        self.phone = phone  # Se não for passado, será None por padrão
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    def update(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }