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
            print(f'{student};\n')
        else:
            print(f'{student},')

def create_instructors(num):
    sentence_insert = f"INSERT INTO INSTRUCTORS (FIRSTNAME,LASTNAME,EMAIL,SALARY)\nVALUES"
    instructors = [(fake.first_name(), fake.last_name(), fake.email(), 
                    random.choice([12000,15000,28000,45000])) for _ in range(num)]
    print(sentence_insert)
    for instructor in instructors:
        if instructor == instructors[-1]:
            print(f'{instructor};\n')
        else:
            print(f'{instructor},')

def create_courses (num, num_instructor):
    # curse_name, description, instructor_ID, duration_hours
    sentence_insert = f"INSERT INTO COURSES (COURSENAME,DESCRIPTION,INSTRUCTORID,DURATIONHOURS)\nVALUES"
    name_courses=['Comunicacion Profesional','Algebra Lineal','Calculo Diferencial E Integral',
                  'Probabilidad','Estadistica','Contabilidad De Costos','Administracion Integral',
                  'Legislacion Informatica','Matematicas Discretas','Fisica Para Informaticos',
                  'Sistemas Digitales','Aplicac. De Sistemas Digitales','Logica De Programacion',
                  'Estructura De Datos','Teoria De La Computacion','Arq. Y Organiz. Computadoras',
                  'Fund. De Programacion O. O.','Programacion Lineal Aplicada','Metodos Numericos',
                  'Presupuestos Y Finanzas','Fundamentos De I. A.','Herramientas Automatizadas',
                  'Fundamentos De Ing. Software','Teleinformatica','Programacion Orientada A Obj.',
                  'Simulacion De Sistemas','Economia','Economia De La Ingenieria',
                  'Ingenieria De Requerimientos','Seguridad Informatica','Construccion De Base De Datos',
                  'Algoritmos Computacionales','Sistemas Operativos','Redes','Dispositivos Programables',
                  'Programacion Web','Seguridad De Software','Diseño De Interfaces',
                  'Admon. De Bases De Datos','Sistemas En Tiempo Real','Compiladores',
                  'Adquisicion De Datos','Calidad Y Normaliz. Software','Seguridad De Redes',
                  'Virologia Y Criptografia','Ingenieria De Pruebas','Administracion De Tecnologias',
                  'Planeacion Estratégica','Ingenieria Del Conocimiento','Ingenieria De Diseño',
                  'Habilidades Directivas','Formulacion Y Evaluacion De Proyectos','Aplicaciones De Redes',
                  'Informatica Empresarial']
    courses = [(name_courses.pop(random.randint(0,len(name_courses)-1)), fake.text(), 
                random.randint(1,num_instructor), random.randint(50,90))for _ in range(num)] 
    print(sentence_insert)
    for course in courses:
        if course == courses[-1]:
            print(f'{course};\n')
        else:
            print(f'{course},')
    namecurso_idinstructor = [(courses[0],courses[2]) for course in courses]
    return namecurso_idinstructor    

def students_courses(num_students,num_courses):
    sentence_insert = f"INSERT INTO STUDENT_COURSE (STUDENTID,COURSEID)\nVALUES"
    student_in_course = []
    pairs = set()
    student_count = {i : 0 for i in range(1,num_students+1)}

    while len(student_in_course)<num_students*7:
        students = random.randint(1,num_students)
        courses = random.randint(1,num_courses)
        if student_count[students]<11 and (students,courses) not in pairs:
            student_in_course.append((students,courses))
            pairs.add((students,courses))
            student_count[students]+=1
    
    print(sentence_insert)
    for pair in student_in_course:
        if pair == student_in_course[-1]:
            print(f'{pair};\n')
        else:
            print(f'{pair},')

create_instructors(15)
create_students(400)
create_courses(25,15)
students_courses(400,25)
