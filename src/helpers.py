import faker


def reg_new_user():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    password = fake.password()
    return name, email, password


print(reg_new_user())
