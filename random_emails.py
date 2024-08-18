import faker

fake = faker.Faker()

emails = []
for _ in range(10):
    name = fake.first_name()
    last_name = fake.last_name()
    email = f"{name.lower()}{last_name.lower()}@gmail.com"
    emails.append(email)

for email in emails:
    print(email)
