## ⚠️ Aviso importante

Este projeto é exclusivamente para fins de estudo em ambiente controlado.

- ❌ Não utilize em dispositivos de terceiros
- ❌ Não execute sem consentimento explícito
- ❌ Não utilize para monitoramento não autorizado

O uso indevido pode violar leis de privacidade e segurança.

## ⚙️ Funcionalidades

### ⌨️ Captura de teclado

- Monitoramento em tempo real das teclas pressionadas
- Diferenciação entre teclas comuns e especiais
- Tratamento de teclas como:
- Espaço
- Enter
- Tab
- Backspace
- Esc

### 📄 Registro em arquivo
- Armazena os dados em log.txt
- Utiliza modo append (não sobrescreve)
- Suporte a caracteres UTF-8

### 📧 Envio automático por e-mail
- Envia os dados capturados periodicamente
- Utiliza protocolo SMTP (Gmail)
- Envio automatizado com Timer

## ▶️ Como usar
1. Instalar dependência

    `pip install pynput`

2. Executar keylogger local, irá salvar dados capturador em um arquivo .txt

    `keylogger.pyw`

3. Executar keylogger com envio por e-mail

    `python keylogger_email.py`

### ⚠️ Antes de executar:

Configure as constantes com dados de um e-mail valido:
- `EMAIL_ORIGEM`
- `EMAIL_DESTINO`
- `SENHA_EMAIL`

## 🧠 Conceitos abordados
- Captura de eventos de teclado
- Manipulação de arquivos
- Programação assíncrona (Listener)
- Automação com threading.Timer
- Envio de e-mails com SMTP
- Tratamento de exceções