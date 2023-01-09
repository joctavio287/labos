import telegram
def mensaje_tel(mensaje: str = 'Termino de correr el script'):
    '''
    Manda un mensaje de telegram al chat que tenes con el bot 'python_scripts'.

    INPUT: 
    mensaje: str: mensaje para mandar al bot.
    '''
    token = '5448153732:AAGhKraJQquEqMfpD3cb4rnTcrKB6U1ViMA'
    chat_id = '1034347542'
    bot = telegram.Bot(token = token)
    bot.sendMessage(chat_id = chat_id, text = mensaje)
if __name__ == '__main__':
    mensaje_tel(mensaje = 'Este es un mensje de prueba')