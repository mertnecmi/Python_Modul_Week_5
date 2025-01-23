# Soru2: Python'da bir "Okul" sınıfı oluşturun. Bu sınıfın aşağıdaki özelliklere ve işlevselliğe sahip olması gerekir:

# Özellikler:
# "isim"
# "kuruluş_yılı"
# "öğrenciler"
# "öğretmenler"
# Yöntemler:
# add_new_student(self, student_name, class): Okula yeni bir öğrenci eklemek için kullanılan bir yöntem. 
# Öğrencinin adını ve sınıfını alır ve "öğrenciler" listesine ekler.
# add_new_teacher(self, teacher_name, branch): Okula yeni bir öğretmen eklemek için kullanılan bir yöntem. 
# Öğretmenin adını ve ana dalını alır ve "teachers" sözlüğüne ekler.
# view_student_list(self): Okulda kayıtlı öğrencilerin listesini görüntülemek için kullanılan bir yöntem. 
# Öğrenci adlarını ve sınıflarını listeleyin.
# view_teacher_list(self): Okulda çalışan öğretmenlerin listesini görüntülemek için kullanılan bir yöntem. 
# Öğretmenlerin adlarını ve ana dallarını listeleyin.

import pandas as pd

class Scholl:
    students = []
    teachers = []
    def __init__(self, school_name, foundation_year):
        self.name   = school_name
        self.fyear  = foundation_year
    def add_new_student(self, student_name, classi):
        self.student    = student_name
        self.classi     = classi
        self.students.append([self.student, self.classi])
    def add_new_teacher(self, teacher_name, branch):
        self.teacher    = teacher_name
        self.branch     = branch
        data =  {
            "Teacher": self.teacher,
            "Branch" : self.branch
            }
        self.teachers.append(data)
        print("Successfull !!!")
    def view_student_list(self):
        print("\n***   STUDENTS LIST   ***")

        for student in self.students:
            print(f"Student Name : {student[0]}  Class : {student[1]}")
    def view_teacher_list(self):
        print("\n***   TEACHERS LIST   ***")
        for teacher in self.teachers:
            print(f"Teacher Name : {teacher["Teacher"]}  Branch : {teacher["Branch"]}")


proje = Scholl("mEHMET aKİF lİSESİ", "1972")
proje.add_new_student("selami","a1")
proje.add_new_student("fatma","c1")

proje.add_new_teacher("Necmi Mert","Zevzeklik")
proje.add_new_teacher("Ali Veli","Denemelik")

proje.view_student_list()
proje.view_teacher_list()