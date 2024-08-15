# Importamos librerias
import random
from faker import Faker 
# Creaciond del objeto
fake = Faker()

def create_students(num):
    sentence_insert = f"INSERT INTO STUDENTS (FIRSTNAME,LASTNAME,AGE,EMAIL)\nVALUES"
    students = [(fake.first_name(), fake.last_name(), random.randint(17,35), fake.email()) for _ in range(num)]
    print(sentence_insert)
    for student in students:
        if student == students[-1]:
            print(f'{student}')
        else:
            print(f'{student},')

def create_instructors(num):
    sentence_insert = f"INSERT INTO INSTRUCTORS (FIRSTNAME,LASTNAME,EMAIL,SALARY)\nVALUES"
    instructors = [(fake.first_name(), fake.last_name(), fake.email(), random.choice([12000,15000,28000,45000])) for _ in range(num)]
    print(sentence_insert)
    for instructor in instructors:
        if instructor == instructors[-1]:
            print(f'{instructor}')
        else:
            print(f'{instructor},')


# create_instructors(5)
# create_students(5)
