class NotepadCreator:
    def __init__(self, filename):
        self.filename = filename
        # Crear o sobrescribir el archivo al iniciar
        with open(self.filename, 'w') as file:
            file.write("")  # Vacía el archivo o lo crea si no existe

    def add_data(self, correo, nombre, usuario):
        with open(self.filename, 'a') as file:
            file.write(f"{correo}:{nombre}:{usuario}\n")

    def save(self):
        print(f"Archivo '{self.filename}' guardado exitosamente.")

# Ejemplo de uso
if __name__ == "__main__":
    filename = "usuarios.txt"
    notepad_creator = NotepadCreator(filename)
      
    notepad_creator.add_data("rara@gmail.com", "suave", "suave2")
    notepad_creator.add_data("pedro@gmail.com", "brillante", "brillante123")
        

    notepad_creator.save()
