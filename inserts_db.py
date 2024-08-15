import random
from faker import Faker 

fake = Faker()

def create_students(num):
    sentence_insert = f"INSERT INTO STUDENTS (FIRSTNAME,LASTNAME,AGE,EMAIL)\nVALUES"
    students = [(fake.first_name(), fake.last_name(), random.randint(17,35), fake.email()) for _ in range(num)]
    return sentence_insert, students


def show_insert_students(sentense, students):
      print(sentense)
      for student in students:
        if student == students[-1]:
            print(f'{student}')
        else:
            print(f'{student},')









sentence, student_list = create_students(5)
show_insert_students(sentence, student_list)
    





