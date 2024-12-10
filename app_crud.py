"""
Arquivo principal para inicialização da aplicação Flask.

Dependências:
    - Flask: Framework web utilizado;
    - models.user: Contém o modelo e a inicialização do banco de dados (SQLAlchemy);
    - routes.user_routes: Define as rotas relacionadas ao recurso "User";
    - config: Contém as configurações do aplicativo para diferentes ambientes.

"""

from flask import Flask
from models.user import db
from routes.user_routes import user_routes
from config import Config, TestConfig, DevConfig, ProdConfig

config_env = 'dev'

def create_app(config_env):
    app = Flask(__name__)

    # Carrega as configurações baseadas no nome do ambiente
    if config_env == 'test':
        app.config.from_object(TestConfig)
    elif config_env == 'dev':
        app.config.from_object(DevConfig)
    elif config_env == 'prod':
        app.config.from_object(ProdConfig)
    else:
        app.config.from_object(Config)  # Padrão se não for passado um ambiente válido
    
    # Inicializa o banco de dados com a app
    db.init_app(app)
    
    # Registra o Blueprint das rotas
    app.register_blueprint(user_routes)
    
    return app

# Garantir que a aplicação seja executada ao rodar o arquivo diretamente
if __name__ == '__main__':
    app = create_app(config_env) 
    
    # Criação das tabelas no banco de dados, caso não existam
    with app.app_context():
        db.create_all()  # Garante que as tabelas sejam criadas antes de iniciar o servidor
    
    app.run(debug=True)  # Inicia o servidor no modo debug