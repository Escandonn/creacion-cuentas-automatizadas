from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
import time

class AutenticacionInterface:
    def esperar_carga_pagina(self):
        pass

    def presionar_boton_obtener_correo(self):
        pass

class Autenticacion(AutenticacionInterface):
    def __init__(self, driver):
        self.driver = driver

    def esperar_carga_pagina(self, tiempo_maximo):
        try:
            WebDriverWait(self.navegador.driver, tiempo_maximo).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print("Página cargada correctamente.")
        except TimeoutException:
            print("La página tardó demasiado en cargar.")
            self.navegador.cerrar_navegador()
   

    def presionar_boton_obtener_correo(self, button_css_selector, input_id):
        try:
            # Wait for the button to be clickable and then click it
            boton_copiar = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, button_css_selector))
            )
            boton_copiar.click()
            print("Botón de copiar presionado.")
            
            # Wait for the input to be available and then get its value
            elemento_input = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, input_id))
            )
            texto = elemento_input.get_attribute("value")
            print(f"El valor del input con ID '{input_id}' es: {texto}")
            return texto
        except TimeoutException:
            print(f"No se pudo encontrar el elemento con el selector '{button_css_selector}' o ID '{input_id}' dentro del tiempo especificado.")
            return None

class Navegador:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Puedes cambiar a otro navegador si lo deseas

    def abrir_pagina(self, url):
        self.driver.get(url)

    def cerrar_navegador(self):
        self.driver.quit()

class CoordinadorAutenticacion:
    def __init__(self, navegador, autenticacion):
        self.navegador = navegador
        self.autenticacion = autenticacion

    def autenticar(self):
        try:
            self.navegador.abrir_pagina("https://temp-mail.org/es/")
            self.autenticacion.esperar_carga_pagina(30)
            self.autenticacion.presionar_boton_obtener_correo()
            
            # self.autenticacion.mantener_sesion(60)  # Mantén la sesión por 60 segundos
        except NoSuchWindowException:
            print("Error: El navegador se cerró inesperadamente.")
        finally:
            self.navegador.cerrar_navegador()


# Uso
navegador = Navegador()
autenticacion = Autenticacion(navegador.driver)
coordinador = CoordinadorAutenticacion(navegador, autenticacion)

coordinador.autenticar()
