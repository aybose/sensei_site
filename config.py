import os

######################################################
# CONFIG PARAMS
######################################################


class BaseConfig:

    #########################
    # SENSEI
    #########################



    #########################
    # Backend
    #########################

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', '')
    if SQLALCHEMY_DATABASE_URI == '':
        SQLALCHEMY_DATABASE_URI = "postgresql://localhost/sensei"
    SECRET_KEY = 'development key'

