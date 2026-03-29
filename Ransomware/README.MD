## ⚠️ Aviso importante

Este projeto é destinado exclusivamente para estudo em ambiente controlado.

- Não utilize em arquivos importantes
-  Não execute fora de ambientes de teste
- A perda da chave (chave.key) torna os arquivos irrecuperáveis

## ⚙️ Como funciona

Antes da criacao do programa, tive que desabilitar o Windows Denfender, pois estava colocando o arquivo em quarentena e posteriormente excluindo.

### 🔒 Criptografia

- Gera uma chave criptográfica (chave.key)
- Procura arquivos dentro da pasta test_files
- Criptografa os arquivos encontrados
- Sobrescreve os arquivos originais
- Cria um arquivo de aviso (LEIA-ME.txt)

### 🔓 Descriptografia

- Utiliza a mesma chave gerada
- Restaura os arquivos ao estado original
- Processa automaticamente todos os arquivos do diretório

## 📂 Estrutura esperada

- │── ransomware.py 
- │── descrypt.py 
- │── test_files/ 
    - ├── arquivo1.txt 
    - ├── arquivo2.jpg

## ▶️ Como usar

1. Instalar dependência

    `pip install cryptography`

2. Criptografar arquivos

    `python ransomware.py`

3. Descriptografar arquivos

    `python decrypt.py`


## 🧠 Conceitos abordados
- Criptografia simétrica (Fernet)
- Manipulação de arquivos binários
- Automação com Python
- Percurso de diretórios com os.walk
- Segurança da informação (conceitos básicos)