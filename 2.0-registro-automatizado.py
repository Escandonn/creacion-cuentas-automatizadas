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
    
    def ingresar_nombre(self, nombre):
        pass

    def ingresar_apellido(self, apellido):
        pass
    
    def hacer_clic_boton_nombre_apellido(self):
        pass


# Clase que implementa la autenticación
class Autenticacion(AutenticacionInterface):
    def __init__(self, driver):
        self.driver = driver

    def ingresar_correo(self, correo):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email-address"))
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
        boton = self.driver.find_element(By.ID, "join-form-submit")
        boton.click()

    def verificar_cambio_de_pagina(self):
        try:
            # Espera hasta que el nuevo elemento esté presente en la página
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h1.main__subtitle"))
            )
            print("SE HA INGRESAO CORRECTAMENTE, AHORA SE SEGUIRA CON REGISTRO DEL  NOMBRE Y APELLIDO")
        except:
            print("No se ha producido cambio de página.")

    def ingresar_nombre(self, nombre):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        for char in nombre:
            username_input.send_keys(char)
            time.sleep(0.5)

    def ingresar_apellido(self, apellido):
        password_input = self.driver.find_element(By.ID, "last-name")
        for char in apellido:
            password_input.send_keys(char)
            time.sleep(0.5)
    
    def hacer_clic_boton_nombre_apellido(self):
        boton = self.driver.find_element(By.ID, "join-form-submit")
        boton.click()

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
        self.navegador.abrir_pagina("https://www.linkedin.com/signup?_l=es")
        self.autenticacion.ingresar_correo(correo)
        self.autenticacion.ingresar_contraseña(contraseña)
        self.autenticacion.hacer_clic_en_boton()
        self.autenticacion.verificar_cambio_de_pagina()
        self.autenticacion.ingresar_nombre("Samuel")
        self.autenticacion.ingresar_apellido("Bernal")
        self.autenticacion.hacer_clic_boton_nombre_apellido()
        print("REGISTRO EXITOSO!")
        # self.navegador.cerrar_navegador()

# Uso
navegador = Navegador()
autenticacion = Autenticacion(navegador.driver)
coordinador = CoordinadorAutenticacion(navegador, autenticacion)

correo = "samen25767@mvpalace.com"
contraseña = "Americano12."

coordinador.autenticar(correo, contraseña)
