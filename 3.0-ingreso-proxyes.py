from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuración del proxy SOCKS4 (reemplaza con el puerto correcto)
proxy = "socks4://166.0.235.197"  # Asegúrate de usar el puerto correcto, en este ejemplo usé 1080

# Configuración de ChromeOptions
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy}')

# Iniciando el navegador con las opciones
driver = webdriver.Chrome(options=chrome_options)

# Abriendo una página web que usa HTTPS a través del proxy
driver.get("https://www.linkedin.com/")

# Interactuar con la página
print(driver.title)

# Cerrar el navegador
driver.quit()
