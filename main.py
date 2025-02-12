from extrator import extrair_titulos
from banco import criar_tabela, salvar_titulos
import interface  # Importa, mas não executa diretamente

def main():
    print("Criando tabela no banco de dados...")
    criar_tabela()
    
    print("Extraindo títulos de notícias...")
    titulos = extrair_titulos()
    
    print("Salvando títulos no banco de dados...")
    salvar_titulos(titulos)
    
    print("Títulos extraídos e salvos com sucesso!")
    print("Agora, execute interface.py para visualizar as notícias.")

if __name__ == "__main__":
    main()
