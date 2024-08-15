import requests
import requests
import random

# Lista de nombres y apellidos predefinidos
names = [
    ("Juan", "Pérez"),
    ("Ana", "García"),
    ("Carlos", "Martínez"),
    ("María", "Lopez"),
    ("Luis", "Fernández")
]

def generate_email(name, surname):
    domain = "1secmail.com"
    username = f"{name.lower()}.{surname.lower()}"
    email = f"{username}@{domain}"
    return email

def create_temp_emails(name_list):
    emails = []
    for name, surname in name_list:
        email = generate_email(name, surname)
        emails.append(email)
        print(f"Correo temporal creado: {email}")
    return emails

def check_inbox(username):
    domain = "1secmail.com"
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}"
    response = requests.get(url)
    messages = response.json()
    
    if messages:
        print("Mensajes en la bandeja de entrada:")
        for message in messages:
            print(f"- ID: {message['id']}, Asunto: {message['subject']}")
    else:
        print("Bandeja de entrada vacía.")

def get_message(username, message_id):
    domain = "1secmail.com"
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={message_id}"
    response = requests.get(url)
    message = response.json()
    
    print(f"De: {message['from']}")
    print(f"Asunto: {message['subject']}")
    print(f"Contenido:\n{message['text']}")

# Crear correos electrónicos temporales
emails = create_temp_emails(names)

# Ejemplo: Revisar la bandeja de entrada para el primer correo electrónico de la lista
username = emails[0].split('@')[0]
check_inbox(username)

# Leer un mensaje específico (usa el ID del mensaje que recuperaste en check_inbox)
# get_message(username, message_id)
