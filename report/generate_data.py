import csv
from faker import Faker
from faker.providers import DynamicProvider

departments_provider = DynamicProvider(
     provider_name="departments",
     elements=["HR", "Finance", "Engineering", "R&D", "IT"],
)
fake = Faker()
fake.add_provider(departments_provider)

def db_generator():
    db = []
    for _ in range(1000):
        item = dict(name=fake.name(), hiring_date=fake.date_between(), department=fake.departments(), birthday=fake.date_of_birth())
        db.append(item)
    return db

def save_db_to_csv(database:list):
    with open('database.csv', 'w') as file:
        writer = csv.writer(file)
        for item in database:
            writer.writerow(item.values())

database = db_generator()
print(database)
save_db_to_csv(database)
