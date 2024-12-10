"""
Arquivo com as configurações necessárias para a aplicação Flask em diferentes ambientes (dev, test, prd)

"""

class Config:
    """
    Configurações base.
    
    Atributos:
        SQLALCHEMY_DATABASE_URI (str): Caminho para o arquivo de banco de dados SQLite utilizado.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Desativa o rastreamento de modificações do SQLAlchemy para melhorar a performance.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data_project.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    """
    Configurações do ambiente de desenvolvimento.

    Herda as configurações base e adiciona:
        SQLALCHEMY_DATABASE_URI (str): Caminho para o banco de dados SQLite utilizado durante o desenvolvimento.
        DEBUG (bool): Ativa o modo de depuração (debug).
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev_data_project.db'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    """
    Configurações do ambiente de teste (qas).

    Herda as configurações base e adiciona:
        SQLALCHEMY_DATABASE_URI (str): Caminho para o banco de dados SQLite utilizado para testes.
        TESTING (bool): Ativa o modo de teste para o Flask.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_data_project.db'
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    """
    Configurações do ambiente de produção.

    Herda as configurações base e garante que o aplicativo esteja otimizado para produção.
    
    Atributos:
        SQLALCHEMY_DATABASE_URI (str): Caminho para o banco de dados SQLite utilizado em produção.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Desativado para manter a performance.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod_data_project.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
