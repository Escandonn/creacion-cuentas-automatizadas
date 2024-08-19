import requests

# Lista de proxies
proxies = [
    {"http": "http://104.129.194.44:8800", "https": "http://104.129.194.44:8800"},
    {"http": "http://104.129.194.99:10686", "https": "http://104.129.194.99:10686"},
    {"http": "http://135.148.100.78:48149", "https": "http://135.148.100.78:48149"},
    {"http": "http://35.185.196.38:3128", "https": "http://35.185.196.38:3128"},
    {"http": "http://162.19.241.220:8091", "https": "http://162.19.241.220:8091"},
    {"http": "http://159.69.41.154:3128", "https": "http://159.69.41.154:3128"},
    {"http": "http://177.234.241.26:999", "https": "http://177.234.241.26:999"},
    {"http": "http://177.234.241.24:999", "https": "http://177.234.241.24:999"},
    {"http": "http://177.234.241.30:999", "https": "http://177.234.241.30:999"},
    {"http": "http://135.181.102.118:7117", "https": "http://135.181.102.118:7117"},
    {"http": "http://89.187.191.121:8888", "https": "http://89.187.191.121:8888"},
    {"http": "http://89.187.191.122:8888", "https": "http://89.187.191.122:8888"},
    {"http": "http://177.234.241.31:999", "https": "http://177.234.241.31:999"},
    {"http": "http://177.234.241.29:999", "https": "http://177.234.241.29:999"},
    {"http": "http://89.187.191.120:8888", "https": "http://89.187.191.120:8888"},
    {"http": "http://178.48.68.61:18080", "https": "http://178.48.68.61:18080"},
    {"http": "http://200.174.198.86:8888", "https": "http://200.174.198.86:8888"},
    {"http": "http://72.10.160.170:30199", "https": "http://72.10.160.170:30199"},
    {"http": "http://212.1.64.147:8080", "https": "http://212.1.64.147:8080"},
    {"http": "http://148.72.140.24:30132", "https": "http://148.72.140.24:30132"},
    {"http": "http://41.65.0.206:1976", "https": "http://41.65.0.206:1976"},
    {"http": "http://144.76.24.28:3128", "https": "http://144.76.24.28:3128"},
    {"http": "http://190.223.60.131:3128", "https": "http://190.223.60.131:3128"},
    {"http": "http://20.204.212.76:3129", "https": "http://20.204.212.76:3129"},
    {"http": "http://160.86.242.23:8080", "https": "http://160.86.242.23:8080"},
    {"http": "http://51.38.230.146:443", "https": "http://51.38.230.146:443"},
    {"http": "http://177.234.241.27:999", "https": "http://177.234.241.27:999"},
    {"http": "http://133.242.171.242:3128", "https": "http://133.242.171.242:3128"},
    {"http": "http://197.164.101.10:1981", "https": "http://197.164.101.10:1981"},
    {"http": "http://20.219.176.57:3129", "https": "http://20.219.176.57:3129"},
    {"http": "http://43.134.1.40:3128", "https": "http://43.134.1.40:3128"},
    {"http": "http://101.255.117.198:8085", "https": "http://101.255.117.198:8085"},
    {"http": "http://164.163.42.19:10000", "https": "http://164.163.42.19:10000"},
    {"http": "http://164.163.42.33:10000", "https": "http://164.163.42.33:10000"},
    {"http": "http://164.163.42.20:10000", "https": "http://164.163.42.20:10000"}
]

# URL de prueba
url = "http://httpbin.org/ip"

# Iterar sobre cada proxy en la lista
for proxy in proxies:
    try:
        # Realiza una solicitud GET a través del proxy
        response = requests.get(url, proxies=proxy, timeout=5)
        
        # Imprime la respuesta JSON con la IP detectada
        print(f"Proxy {proxy['http']} -> {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el proxy {proxy['http']}: ")
