"""
Neste arquivo é definido as rotas relacionadas a entidade 'User' para aplicação Flask.

Rotas:
    POST /users:
        Cria um novo usuário.

    GET /users:
        Retorna todos os usuários cadastrados.

    GET /users/<int:id>:
        Retorna um usuário específico com base no ID fornecido.

    PUT /users/<int:id>:
        Atualiza os dados de um usuário existente com base no ID.

    DELETE /users/<int:id>:
        Exclui um usuário com base no ID fornecido.

Obs: As respostas seguem o padrão JSON para facilitar a comunicação com a aplicação cliente.

"""

from flask import Blueprint, request, jsonify
from models.user import db, User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['POST'])
def create_user():
    # Pega os dados enviados no corpo da requisição
    data = request.get_json()

    # Valida se os dados necessários estão presentes
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({'Error': 'Os campos name e email são necessários'}), 400  # Retorna erro 400 se faltar nome ou email

    # Cria o novo usuário, o 'phone' é opcional e pode ser None (vazio)
    new_user = User(name=data['name'], email=data['email'], phone=data.get('phone'))

    try:
        # Salva o novo usuário no banco de dados
        new_user.save()
    except Exception as e:
        return jsonify({'Error': 'Erro ao criar novo usuário.', 'error': str(e)}), 500  # Retorna erro 500 se houver falha no banco de dados

    # Retorna a resposta com os dados do novo usuário e código de status 201 (Created)
    return jsonify({
        'id': new_user.id,
        'name': new_user.name,
        'phone': new_user.phone,
        'email': new_user.email
    }), 201

@user_routes.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.get_all_users()
        print(users)  # Verifica se os usuários estão sendo recuperados
        result = jsonify([user.to_dict() for user in users])
    except Exception as e:
        print(f"Erro: {e}")
        result = jsonify({'Error': 'Não foi possível retornar todos os usuários.', 'Details': str(e)}), 500
    return result

@user_routes.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.get_user_by_id(id)
    except Exception as e:
        return jsonify({'Error': 'Não foi possível encontrar o usuário.'})
    if not user:
        return jsonify({'Error': 'Usuário não encontrado'}), 404
    return jsonify(user.to_dict())

@user_routes.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.get_user_by_id(id)
    except Exception as e:
        return jsonify({'Error': 'Não foi possível encontrar o usuário.'})
    if not user:
        return jsonify({'Error': 'Usuário não encontrado'}), 404
    
    try:
        data = request.get_json()

        # Verifica se os dados que estão sendo passados são válidos
        name = data.get('name', user.name)  # Se 'name' não for fornecido, mantém o atual
        email = data.get('email', user.email)  # Mesmo para 'email'
        phone = data.get('phone', user.phone)  # Se 'phone' não for fornecido, mantém o atual
        
        user.update(name=name, email=email, phone=phone)
        result = jsonify(user.to_dict())
    except Exception as e:
        result = jsonify({'Error': 'Não foi possível atualizar o usuário'})
    return result

@user_routes.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.get_user_by_id(id)
    except Exception as e:
        return jsonify({'Error': 'Não foi possível encontrar o usuário.'})
    if not user:
        return jsonify({'Error': 'Usuário não encontrado'}), 404
    
    try:
        user.delete()
        return jsonify({'Info': 'Usuário excluído com sucesso'}), 204
    except Exception as e:
        return jsonify({'Error': 'Não foi possível excluir o usuário'}), 500
