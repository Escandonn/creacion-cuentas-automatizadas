import faker
fake = faker.Faker()
import pandas as pd

data = []
for _ in range(1):
    name = fake.first_name()
    last_name = fake.last_name()
    email = f"{name.lower()}{last_name.lower()}@gmail.com"
    data.append({'Nombre': name, 'Apellido': last_name, 'Correo': email})

matrix = pd.DataFrame(data)
print(matrix)
