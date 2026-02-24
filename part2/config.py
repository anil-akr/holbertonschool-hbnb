class Config:
    DEBUG = False
    SECRET_KEY = 'your-secret-key'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
