from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicialização da aplicação Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecomerce.db'

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

# Definição do modelo
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

# Definição de uma rota
@app.route('/')
def hello_world():
    return 'Hello World'

# Função para fornecer o contexto do shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Product': Product}

# Execução da aplicação
if __name__ == "__main__":
    app.run(debug=True)
