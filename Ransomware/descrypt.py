from cryptography.fernet import Fernet
import os  

# Carregando chave
def carregar_chave():
    return open("chave.key", "rb").read()


# Descriptografar arquivo
def descriptografar_arquivo(arquivo, chave):
    with open(arquivo, "rb") as file:
        dados = file.read() # Lendo arquivo e colocando seus dados em uma variavel
    dados_descriptografados = chave.decrypt(dados) # Descriptografando arquivos
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados) # Sobrescrevendo arquivo com dados originais

# Encontrar arquivos para descriptografar
def encontrar_arquivos(diretorio):
    lista_arquivos = []
    for raiz, _, arquivos in os.walk(diretorio): # Andando pelo diretorio
        for nome in arquivos:
            caminho = os.path.join(raiz, nome) # Identificando e atribuindo path para variavel
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista_arquivos.append(caminho) # Adicionando em uma lista os paths encontrados
    return lista_arquivos


# Execucao
def main():
    chave = carregar_chave()
    cofre = Fernet(chave) # Variavel que sera o cofre para guardar dados
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, cofre)
    print("ARQUIVOS RESTAURADOS!")

if __name__ == "__main__":
    main() 