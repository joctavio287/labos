import requests

def mensaje_tel(api_token:str, chat_id: str, mensaje: str = 'Termino de correr el script'):
    '''
    Manda un mensaje de telegram al chat que tenes con el bot 'python_scripts'.
    
    El API token se saca del chat con BotFather. Para obtener el ID del chat us
    ar el siguiente código. Si no funciona borrar el chat con el bot, inicializ
    ar de nuevo y probar nuevamente.

    >>url = f'https://api.telegram.org/bot{token}/getUpdates'
    >>print(requests.get(url).json())
    
    INPUT:
    api_token: str: token del bot creado.
    chat_id: str: id del chat al que queres mandar el mensaje. 
    mensaje: str: mensaje para mandar al bot.
    '''
    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    try:
        response = requests.post(api_url, json={'chat_id': chat_id, 'text': mensaje})
        return response.text
    except Exception as e:
        return e

if __name__ == '__main__':
    # El API token se saca de BotFather
    # How to get the chat_id
    # url = f'https://api.telegram.org/bot{token}/getUpdates'
    # print(requests.get(url).json())
    
    
    