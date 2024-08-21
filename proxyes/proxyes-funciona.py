import requests
import threading

def cargar_proxies_desde_archivo(ruta_archivo):
    proxies = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                proxy = {"http": f"http://{linea}", "https": f"http://{linea}"}
                proxies.append(proxy)
    return proxies

def probar_proxy(proxy, url):
    try:
        response = requests.get(url, proxies=proxy, timeout=5)
        ip = response.json()['origin']
        proxy_ip = proxy['http'].split(':')[1][2:]
        print(proxy_ip)
    except requests.exceptions.RequestException as e:
        pass
    except KeyError as e:
        pass
    except Exception as e:
        pass

def probar_proxies(proxies, url):
    threads = []
    for proxy in proxies:
        thread = threading.Thread(target=probar_proxy, args=(proxy, url))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def main():
    ruta_archivo_proxies = 'proxyes/proxies.txt'  # Cambia esto por la ruta a tu archivo de proxies
    url_prueba = "http://httpbin.org/ip"
    
    # Cargar proxies desde el archivo
    proxies = cargar_proxies_desde_archivo(ruta_archivo_proxies)
    
    # Probar cada proxy
    probar_proxies(proxies, url_prueba)

if __name__ == "__main__":
    main()