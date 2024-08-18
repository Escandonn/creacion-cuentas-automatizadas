from fake import FAKER


nombre = FAKER.first_name()
apellido = FAKER.apellido()
usuario = FAKER.username()

nombre_completo = f"{nombre} {apellido}"
print(usuario)

