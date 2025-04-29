from fakepinterest import database, app
from fakepinterest.models import *

with app.app_context():
    database.create_all()

# para criar o DB, basta executa este arquivo create_database.py