import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Interface para la autenticación
class AutenticacionInterface:
    def ingresar_correo(self, correo):
        pass



    def ingresar_contraseña(self, contraseña):
        pass

    def hacer_clic_en_boton(self):
        pass

    def verificar_cambio_de_pagina(self):
        pass

# Clase que implementa la autenticación
class Autenticacion(AutenticacionInterface):
    def __init__(self, driver):
        self.driver = driver

    def ingresar_correo(self, correo):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        for char in correo:
            username_input.send_keys(char)
            time.sleep(0.5)

    def ingresar_contraseña(self, contraseña):
        password_input = self.driver.find_element(By.ID, "password")
        for char in contraseña:
            password_input.send_keys(char)
            time.sleep(0.5)

    def hacer_clic_en_boton(self):
        boton = self.driver.find_element(By.XPATH, "//button[@data-litms-control-urn='login-submit']")
        boton.click()

    def verificar_cambio_de_pagina(self):
        tiempo_inicio = time.time()
        while time.time() - tiempo_inicio < 5:  # Esperar 5 segundos
            if self.driver.title!= "Iniciar sesión | LinkedIn":
                print("La página ha cambiado")
                break
            time.sleep(1)
        else:
            print("No se ha producido cambio de página")

# Clase que configura el navegador
class Navegador:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Puedes cambiar a otro navegador si lo deseas

    def abrir_pagina(self, url):
        self.driver.get(url)

    def cerrar_navegador(self):
        self.driver.quit()

# Clase que coordina la autenticación
class CoordinadorAutenticacion:
    def __init__(self, navegador, autenticacion):
        self.navegador = navegador
        self.autenticacion = autenticacion

    def autenticar(self, correo, contraseña):
        self.navegador.abrir_pagina("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
        self.autenticacion.ingresar_correo(correo)
        self.autenticacion.ingresar_contraseña(contraseña)
        self.autenticacion.hacer_clic_en_boton()
        self.autenticacion.verificar_cambio_de_pagina()
        self.navegador.cerrar_navegador()


# Uso
navegador = Navegador()
autenticacion = Autenticacion(navegador.driver)
coordinador = CoordinadorAutenticacion(navegador, autenticacion)

correo = "samen25767@mvpalace.com"
contraseña = "Americano12."

coordinador.autenticar(correo, contraseña)