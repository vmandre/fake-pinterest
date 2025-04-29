from fakepinterest import database, app
from fakepinterest.models import *

with app.app_context():
    database.create_all()

# para criar o DB, basta executar este arquivo: python3 create_database.py