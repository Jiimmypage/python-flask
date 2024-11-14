from app import app, db
from sqlalchemy import text

def delete_products_table():
    with app.app_context():  # Adiciona o contexto da aplicação
        try:
            # Usar text() para declarar a expressão SQL
            db.session.execute(text("DROP TABLE IF EXISTS product"))
            db.session.commit()
            print("Tabela 'product' excluída com sucesso.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    delete_products_table()
