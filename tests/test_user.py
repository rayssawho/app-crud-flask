"""
Arquivo para os testes unitários na aplicação Flask

"""

import unittest
from app_crud import create_app, db
from models.user import User


class UserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Configura o ambiente antes dos testes."""
        cls.app = create_app('test')  # Usando o ambiente de testes
        cls.client = cls.app.test_client()  # Cria um cliente para fazer requisições HTTP
        cls.app_context = cls.app.app_context()  # Cria o contexto da aplicação
        cls.app_context.push()  # Empurra o contexto da aplicação para a pilha

        db.create_all()  # Cria todas as tabelas no banco de dados

    @classmethod
    def tearDownClass(cls):
        """Limpa o ambiente depois dos testes."""
        db.session.remove()  # Remove a sessão do banco
        db.drop_all()  # Droppa todas as tabelas
        cls.app_context.pop()  # Remove o contexto da aplicação

    def setUp(self):
        """Executa antes de cada teste."""
        # Adiciona um usuário para os testes
        self.test_user = User(name="Test User", phone=123456789, email="test_user@example.com")
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self):
        """Executa após cada teste."""
        db.session.query(User).delete()
        db.session.commit()

    def test_create_user(self):
        """Teste para criar um usuário."""
        response = self.client.post('/users', json={
            'name': 'Usuário-Teste da Silva',
            'phone': 968596851,
            'email': 'user_silva@yahoo.com'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('name', response.json)
        self.assertIn('phone', response.json)
        self.assertIn('email', response.json)

    def test_get_all_users(self):
        """Teste para obter todos os usuários."""
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertGreaterEqual(len(response.json), 1)

    def test_get_user_by_id(self):
        """Teste para obter um usuário por ID."""
        response = self.client.get(f'/users/{self.test_user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Test User')
        self.assertEqual(response.json['email'], 'test_user@example.com')

    def test_update_user(self):
        """Teste para atualizar um usuário."""
        response = self.client.put(f'/users/{self.test_user.id}', json={
            'name': 'Updated User',
            'phone': 987654321,
            'email': 'updated_user@example.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Updated User')
        self.assertEqual(response.json['phone'], 987654321)
        self.assertEqual(response.json['email'], 'updated_user@example.com')

    def test_delete_user(self):
        """Teste para excluir um usuário."""
        response = self.client.delete(f'/users/{self.test_user.id}')
        self.assertEqual(response.status_code, 204)

        # Verifica se o usuário foi realmente excluído
        response = self.client.get(f'/users/{self.test_user.id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
