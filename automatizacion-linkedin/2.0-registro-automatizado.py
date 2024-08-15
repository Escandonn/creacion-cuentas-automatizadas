import requests
import time
import re

def check_inbox(username):
    domain = "1secmail.com"
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}"
    response = requests.get(url)
    messages = response.json()
    
    if messages:
        for message in messages:
            # Filtrar mensajes de verificación de Instagram
            if 'instagram' in message['subject'].lower():
                print(f"Correo de verificación encontrado con ID: {message['id']}")
                return message['id']
    return None

def get_message(username, message_id):
    domain = "1secmail.com"
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={message_id}"
    response = requests.get(url)
    message = response.json()
    
    # Verifica las posibles claves donde podría estar el contenido del mensaje
    if 'text' in message:
        return message['text']
    elif 'body' in message:
        return message['body']
    else:
        raise KeyError("El contenido del mensaje no se encuentra en las claves esperadas.")

def extract_verification_code(message_text):
    # Utilizar expresión regular para encontrar un código de verificación en el correo
    match = re.search(r'\b\d{6}\b', message_text)  # Ajusta el patrón según el formato del código
    if match:
        return match.group(0)
    return None

# Dirección de correo temporal que utilizaste para el registro
email = "anastacia.cucurella@1secmail.com"
username = email.split('@')[0]

# Esperar y verificar la bandeja de entrada
print("Esperando correo de verificación...")
while True:
    message_id = check_inbox(username)
    if message_id:
        message_content = get_message(username, message_id)
        verification_code = extract_verification_code(message_content)
        if verification_code:
            print(f"Código de verificación recibido: {verification_code}")
        else:
            print("Código de verificación no encontrado en el mensaje.")
        break
    time.sleep(30)  # Esperar 30 segundos antes de volver a comprobar
