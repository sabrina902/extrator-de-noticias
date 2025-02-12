import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="noticias_db"
    )

def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS noticias (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo TEXT NOT NULL,
            data_extracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conexao.commit()
    cursor.close()
    conexao.close()

def salvar_titulos(titulos):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    for titulo in titulos:
        cursor.execute("INSERT INTO noticias (titulo) VALUES (%s)", (titulo,))
    
    conexao.commit()
    cursor.close()
    conexao.close()

def obter_titulos():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT titulo FROM noticias ORDER BY data_extracao DESC")
    titulos = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    return [titulo[0] for titulo in titulos]

# Teste rápido
if __name__ == "__main__":
    criar_tabela()
