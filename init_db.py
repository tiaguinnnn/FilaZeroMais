import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def configurar_banco():
    print("🚀 [DevOps] Iniciando provisionamento do banco de dados...")
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'VoucherDev@2024')
        )
        cursor = conn.cursor()
        db_name = os.getenv('DB_NAME', 'filazero_db')
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4;")
        print(f"✅ Banco de dados '{db_name}' pronto para uso!")
        conn.close()
    except Exception as e:
        print(f"❌ Erro no banco: {e}")

if __name__ == "__main__":
    configurar_banco()