# from lib2to3.pgen2 import driver
from lib2to3.pgen2 import driver
import time
from httpcore import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



# Interface para la autenticación
class AutenticacionInterface:
    def ingresar_correo(self, correo):
        pass

    def ingresar_nombre_completo(self, nombreCom):
        pass

    def ingresar_nombre_usuario(self, nombreUsuario):
        pass

    def ingresar_contraseña(self, contrase):
        pass

    def hacer_clic_en_boton(self):
        pass
    
    def verificar_cambio_de_pagina(self):
        pass

    def ingresar_mes(self):
        
        pass

    def ingresar_dia(self):
        
        pass

    def ingresar_año(self):
        
        pass

    def hacer_clic_en_boton_fecha(self):
         
         pass
    
    
    def mantener_sesion(self):
         
         pass

    
    def verificar_cambio_de_pagina_fecha(self):
         
         pass
    
    


# Clase que implementa la autenticación
class Autenticacion(AutenticacionInterface):
    def __init__(self, driver):
        self.driver = driver

    def ingresar_correo(self, correo):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "emailOrPhone"))
        )
        for char in correo:
            username_input.send_keys(char)
            time.sleep(0.5)

    def ingresar_nombre_completo(self, nombreCom):
        password_input = self.driver.find_element(By.NAME, "fullName")
        for char in nombreCom:
            password_input.send_keys(char)
            time.sleep(0.5)

    def ingresar_nombre_usuario(self, nombreUsuario):
        password_input = self.driver.find_element(By.NAME, "username")
        for char in nombreUsuario:
            password_input.send_keys(char)
            time.sleep(0.5)

    def ingresar_contraseña(self,contrase):
        password_input = self.driver.find_element(By.NAME, "password")
        for char in contrase:
            password_input.send_keys(char)
            time.sleep(0.5)

    def hacer_clic_en_boton(self):
        try:
            # Esperar hasta que el botón "Registrarte" sea visible y esté habilitado
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "_acan _acap _acas _aj1- _ap30") and @type="submit" and text()="Registrarte"]'))
            )

            # Hacer clic en el botón
            button.click()

        except TimeoutException:
            print("El botón 'Registrarte' no se encontró en el tiempo especificado.")
        except Exception as e:
            print(f"Error al intentar hacer clic en el botón 'Registrarte': {e}")
    
    def verificar_cambio_de_pagina(self):
        try:
            # Espera hasta que el nuevo elemento con el span específico esté presente en la página
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.x1s688f.x5n08af.x2b8uid.x1tu3fi.x3x7a5m.x10wh9bi.x1wdrske.x8viiok.x18hxmgj[dir="auto"]'))
            )
            print("SE HA INGRESADO CORRECTAMENTE, AHORA SE SEGUIRÁ CON EL REGISTRO DEL NOMBRE Y APELLIDO")
        
        except Exception as e:
            print("No se ha producido cambio de página.", e)
    
    def ingresar_mes(self,mes):
        try:
                # Localizar el menú desplegable de mes
                select_element = self.driver.find_element(By.CSS_SELECTOR, 'select._aau-._ap32[title="Mes:"]')
                
                # Crear una instancia de Select con el elemento del menú desplegable
                select = Select(select_element)
                
                # Seleccionar la opción basada en el valor proporcionado
                select.select_by_value(str(mes))
                
                print(f"El mes '{mes}' ha sido seleccionado correctamente.")
    
        except Exception as e:
                print(f"No se pudo seleccionar el mes '{mes}'.", e)
    
    def ingresar_dia(self,dia):
        try:
                # Localizar el menú desplegable de mes
                select_element = self.driver.find_element(By.CSS_SELECTOR, 'select._aau-._ap32[title="Día:"]')
                
                # Crear una instancia de Select con el elemento del menú desplegable
                select = Select(select_element)
                
                # Seleccionar la opción basada en el valor proporcionado
                select.select_by_value(str(dia))
                
                print(f"El mes '{dia}' ha sido seleccionado correctamente.")
    
        except Exception as e:
                print(f"No se pudo seleccionar el mes '{dia}'.", e)
    

    def ingresar_año(self, año):
        try:
                # Localizar el menú desplegable de mes
                select_element = self.driver.find_element(By.CSS_SELECTOR, 'select._aau-._ap32[title="Año:"]')
                
                # Crear una instancia de Select con el elemento del menú desplegable
                select = Select(select_element)
                
                # Seleccionar la opción basada en el valor proporcionado
                select.select_by_value(str(año))
                
                print(f"El mes '{año}' ha sido seleccionado correctamente.")
    
        except Exception as e:
                print(f"No se pudo seleccionar el mes '{año}'.", e)

    
    def hacer_clic_en_boton_fecha(self):
        try:
            # Esperar hasta que el botón "Siguiente" sea visible
            button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//button[contains(@class, "_acan _acap _acaq _acas _aj1- _ap30") and text()="Siguiente"]'))
            )

            # Esperar hasta que el botón esté habilitado
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "_acan _acap _acaq _acas _aj1- _ap30") and text()="Siguiente" and not(@disabled)]'))
            )

            # Hacer clic en el botón
            button.click()

        except TimeoutException:
            print("El botón 'Siguiente' no se encontró en el tiempo especificado o no se habilitó.")
        except Exception as e:
            print(f"Error al intentar hacer clic en el botón 'Siguiente': {e}")

    def mantener_sesion(self, duracion_segundos):
        try:
            print(f"Manteniendo la sesión activa durante {duracion_segundos} segundos...")
            time.sleep(duracion_segundos)
        except KeyboardInterrupt:
            print("Sesión terminada manualmente.")
        finally:
            self.cerrar_navegador()
            print("Navegador cerrado.")


    def verificar_cambio_de_pagina_fecha(self):
        try:
            # Espera hasta que el nuevo elemento con el span específico esté presente en la página
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//span[contains(@class, "x1lliihq x1plvlek xryxfnj x1n2onr6") and contains(@class, "x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x") and contains(text(), "Introduce el código de confirmación")]'))
            )
            print("SE HA INGRESADO CORRECTAMENTE, AHORA SE SEGUIRÁ CON EL PROCESO DE AUTENTICACIÓN DE CORREO")
        
        except Exception as e:
            print("No se ha producido cambio de página.", e)


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

    def autenticar(self, correo, nombreCompleto, nombreUsuario, contraseña):
        self.navegador.abrir_pagina("https://www.instagram.com/accounts/emailsignup/")
        self.autenticacion.ingresar_correo(correo)
        self.autenticacion.ingresar_nombre_completo(nombreCompleto)
        self.autenticacion.ingresar_nombre_usuario(nombreUsuario)
        self.autenticacion.ingresar_contraseña(contraseña)
        self.autenticacion.hacer_clic_en_boton()
        self.autenticacion.verificar_cambio_de_pagina()
        self.autenticacion.ingresar_mes(8)
        self.autenticacion.ingresar_dia(25)
        self.autenticacion.ingresar_año(1987)
        self.autenticacion.hacer_clic_en_boton_fecha()
        # self.autenticacion.mantener_sesion(5)
        self.autenticacion.verificar_cambio_de_pagina_fecha()
        print("REGISTRO EXITOSO!")
        # self.navegador.cerrar_navegador()

# Uso
navegador = Navegador()
autenticacion = Autenticacion(navegador.driver)
coordinador = CoordinadorAutenticacion(navegador, autenticacion)

correo = "samen25767@mvpalace.com"
nombreCompleto = "Samantha Nicolás"
nombreUsuario = "samanthannicolas"
contraseña = "Americano12."


coordinador.autenticar(correo,nombreCompleto,nombreUsuario,contraseña)
