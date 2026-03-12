class Config:
    DEBUG = False
    SECRET_KEY = 'your-secret-key'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

class Config:

    SECRET_KEY = "secret-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///hbnb.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "jwt-secret"
