import os

db_host = os.environ.get('POSTGRES_HOST', default='localhost')
db_name = os.environ.get('POSTGRES_NAME', default='notes')
db_user = os.environ.get('POSTGRES_USERNAME', default='notes')
db_password = os.environ.get('POSTGRES_PASSWORD', default='')
db_port = os.environ.get('POSTGRES_PORT', default='5432')

# to supress the warnings
SQLALCHEMY_TRACK_MODIFICATIONS = False

# to connect to database env
SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
