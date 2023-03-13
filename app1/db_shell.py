# exec(open(r'D:\Ashwini.doc\Django_env\first_project\app1\db_shell.py').read())

from app1.models import *
from django.contrib.auth.models import User


# to get all data
objs = Person.objects.all()
# print(list(objs))
# print(objs.query)             # if we will check query #SELECT "person"."id", "person"."name", "person"."age", "person"."mobile_no", "person"."address" FROM "person"

for person in objs:
    print(person)
    print(person.__dict__)   #for dict

# to get first /single records
# first_record = Person.objects.first()
# print(first_record)

# to get record by id
# obj = Person.objects.get(id=3)     #single record
# print(obj)

# if person not persent in table that time error is does not exsit if we will handhle this error do this
# try:
#     obj = Person.objects.get(id=4)     #single record
#     print(obj)

# except Person.DoesNotExist:  
#     print("Record does not exist.")

# to get multiple record by passing fielname
# objs = Person.objects.filter(age=23 , name = "lmn")         #, and 
# print(objs.__dict__)
# print(objs.query)

# modify existing data
# p1 = Person.objects.get(id=5)
# print(p1.__dict__)
# update data
# p1.mobile_no = 2356897412
# print(p1.__dict__)
# p1.save()                     

# delete data in database
# p1 = Person.objects.get(id=5)
# p1.delete()

# create data base
# save - 1st way-
# p1 = Person(name="ABC", age=29, mobile_no=5689321478, address="kalkota")
# p1.save()

#2nd way to save data
# p2 = Person.objects.create(name="pranita", age=28, mobile_no=5689561478, address="morshi")
# p2.save()




# exec(open(r'D:\Ashwini.doc\Django_env\first_project\app1\db_shell.py').read())
# print(dir(Person.objects))
# '_constructor_args', '_db', '_get_queryset_methods', '_hints', '_insert', '_queryset_class', '_set_creation_counter',
#   '_update', 'aaggregate', 'abulk_create', 'abulk_update', 'acontains', 'acount', 'acreate', 'aearliest', 
#   'aexists', 'aexplain', 'afirst', 'aget', 'aget_or_create', 'aggregate', 'ain_bulk', 'aiterator', 'alast', 
#   'alatest', 'alias', 'all', 'annotate', 'aupdate', 'aupdate_or_create', 'auto_created', 'bulk_create', 'bulk_update', 
#   'check', 'complex_filter', 'contains', 'contribute_to_class', 'count', 'create', 'creation_counter', 'dates', 'datetimes',
#    'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 
#    'filter', 'first', 'from_queryset', 'get', 'get_or_create', 'get_queryset', 'in_bulk', 'intersection', 'iterator', 'last', 
#    'latest', 'model', 'name', 'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update',
#  'select_related', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list']




# bulk_create
# p1 = Person(name="P", age=26, mobile_no=78, address="Thane")
# p2 = Person(name="Q", age=22, mobile_no=79, address="Napur")
# p3 = Person(name="R", age=28, mobile_no=76, address="Channai")
# p4 = Person(name="S", age=24, mobile_no=75, address="indore")
# p5 = Person(name="T", age=27, mobile_no=14, address="Hydrabad")
# Person.objects.bulk_create([p1, p2, p3, p4, p5 ])

# count person in database
# print(Person.objects.count())

# to delete all records
# Person.objects.all().delete()

# to delete multiple records
# Person.objects.filter(age=22).delete()

# startswith and endwith operation
# print(Person.objects.filter(name__startswith="P"))
# print(Person.objects.filter(name__endswith="a"))

# exculde data
# print(Person.objects.exclude(name__startswith="T"))

#exists   True,False
# print(Person.objects.filter(id=1).exists())  #True

# print(Person.objects.filter(id=100).exists())  #False

# order_by data
# print(Person.objects.all().order_by("id"))         #accending order
# print(Person.objects.all().order_by("-id"))        #decending order

# for contain
# print(Person.objects.filter(name__contains="r"))
# ----------------------------------------------------------------------------------------
# Data = Person.objects.all().values()

# Data = Person.objects.all().values("id","name")
# print(Data.__dict__)
# print(Data)
# name_list = []
# for i in Data:
    # print(i,type(i))
    # name_list.append(i["name"])
# print(name_list)
#---------------------------------------------------------------------------------------------
# Data = Person.objects.all().values("id","name","age")        #list of dict
# print(list(Data))
# print(list(map(lambda x: x['age'],list(Data))))

#-------------------------------------------------------------------------------------------
# avarage age of all person
# Data = Person.objects.all().values("id","name","age")
# lst = list(map(lambda x: x['age'],list(Data)))
# print(sum(lst)//len(lst))
#---------------------------------------------------------------------------------------------
# Data = Person.objects.all().values_list("id","name","age")    #list of tuple
# print(list(Data))

# Data = Person.objects.all().values_list("name")    #list of tuple containg value only
# print(list(Data))





#--------------------------------------------------------------------------------------------------
#changes models file
# Person.objects.get(id=1).show_details()

# for per_obj in Person.objects.all():
    # per_obj.show_details()

# print(Person.get_data_above_age())

# print(Person.get_avg_age())

#--------------------------------------------------------------------------------------------
#=========================================================================================
# change database mysql
# exec(open(r'D:\Ashwini.doc\Django_env\first_project\app1\db_shell.py').read())

# User.objects.create_user(username="kalyani", password="python@12")      #always user create_user for creating new user


# p1 = Person.objects.all()
# print(p1)

#update data
# p1 = Person.objects.get(id=3)
# p1.is_active = True
# p1.save()

# p1 = Person.objects.get(id=3)
# p1.is_active = False
# p1.save()

# data = Person.objects.filter(id__in=[3, 5, 6]).update(is_active=False)
# print(data)

# for multiple updateing
# data = Person.objects.all().update(is_active=False)
# print(data)

# data = Person.objects.all().update(is_active=True)
# print(data)

# for get active or inactive data
# print(Person.objects.filter(is_active=False))
# print(Person.objects.filter(is_active=True))

#get active and inactive data using method in models.py file
# print(Person.get_active_data())           
# print(Person.get_inactive_data())       

# get active and inactive data using class in models.py file
# print(Person.activep.all())
# print(Person.inactivep.all())

# print(Person.all_data.all())--------------------------------------objects
#-----------------------------------------------------------------------------------------------------
# exec(open(r'D:\Ashwini.doc\Django_env\first_project\app1\db_shell.py').read())
# collg = College.objects.all()  
# pric = Principal.objects.all()
# depts = Department.objects.all()
# student = Student.objects.all()
# subs = Subjects.objects.all()
# # print([collg, pric, dept, student, sub])
# print(collg)
# print(pric)
# print(depts)
# print(student)
# print(subs)

# depts = Department.objects.all()
# for dept in depts:
#     # print(dept)
#     print(dept.__dict__)

# collg = College.objects.all()
# for colg in collg:
#     print(colg.__dict__)

# pric = Principal.objects.all()
# for prin in pric:
#     print(prin.__dict__)

# student = Student.objects.all()
# for stud in student:
#     print(stud.__dict__)

# subs = Subjects.objects.all()
# for subject in subs:
#     print(subject.__dict__)

collg = College.objects.all()
clg = collg[0]
# print(clg)
# to get the principal in colg
# print(clg.princi.__dict__)

# print(Principal.objects.first())

# principal se colg nikalnay liye
# savita_objects = Principal.objects.first()
# print(savita_objects.college)

# select related

# print(dir(clg))

# print(clg.department_set.all())        #onetomany relationship

# dept = Department.objects.first()
# print(dept.college)

# dept = Department.objects.get(id=3)
# print(dept.college)

# # get third department student
dept = Department.objects.get(id=3)
print(dept.studs.all())
# print(dir(dept))




# get all student in all dept

# all_depts = Department.objects.all()
# for dept in all_depts:
    # print(dept)
    # print(f"Department Name:- {dept.name},Studs:- {list(dept.student_set.all())}")

# all_depts = Department.objects.all()
# d = {}
# for dept in all_depts:
#     d[dept.name] = list(dept.student_set.all())
# print(d)
#--------------------------------------------------------------------------------   
# s1 = Student.objects.all()
# print(s1)
# s1 = Student.objects.first()
# print(s1)
# s1 = Student.objects.get(id=4)
# print(s1)
# print(s1.dept)

# get dept from student
# studs = Student.objects.all()
# stud_dept_dict = {}
# # print(studs)
# for stud in studs:
#     stud_dept_dict[stud.name] = stud.dept.name
# print(stud_dept_dict)
#{'Rina': 'EE', 'soloni': 'EE', 'mayuri': 'EE', 'prajkata': 'IT', 'dipali': 'IT', 'swati': 'IT', 'swata': 'Civil', 'rahul': 'Civil', 'anjali': 'Civil'}  
#---------------------------------------------------------------------------------
# exec(open(r'D:\Ashwini.doc\Django_env\first_project\app1\db_shell.py').read())

# clgs  = College.objects.get(id=1)
# print(clgs.princi)
# print(clgs.depts.all())

# depts = Department.objects.all()
# for dept in depts:
#     print(dept.subjs.all())
# print(dept.dept.subjs.all()for dept in Department.objects.all())

# clg se IT kay student
# clg = College.objects.get(id=1)
# # print(clg.depts.all()[1])
# print(clg.depts.all()[1].studs.all())
# print(clg.depts.all()[1].studs.all()[0])
# print(clg.depts.all()[2].studs.all())

# clg = College.objects.get(id=1)
# stud_list =[]
# for dept in clg.depts.all():
#     stud_list.append(dept.studs.all())
# print(stud_list)
#[<QuerySet [<Student: Rina>, <Student: soloni>, <Student: mayuri>]>, <QuerySet [<Student: prajkata>, <Student: dipali>, <Student: swati>]>, 
#<QuerySet [<Student: swata>, <Student: rahul>, <Student: anjali>]>]    
#-------------------------------------------------------------------------------------
# clg = College.objects.get(id=1)
# stud_list =[]
# for dept in clg.depts.all():
#     stud_list.extend(dept.studs.all())
# print(stud_list)
# [<Student: Rina>, <Student: soloni>, <Student: mayuri>, <Student: prajkata>, <Student: dipali>, 
# <Student: swati>, <Student: swata>, <Student: rahul>, <Student: anjali>]


# stud_list = []
# for dept in College.objects.get(id=1).depts.all():
    
#     stud_list.extend(dept.studs.all())
# print(stud_list)
#[<Student: Rina>, <Student: soloni>, <Student: mayuri>, <Student: prajkata>, <Student: dipali>, <Student: swati>,
#  <Student: swata>, <Student: rahul>, <Student: anjali>]


# s1 = Student.objects.get(id=5)
# print(s1.dept)                    #dipali
# print(s1.dept.college)           #D Y Patil
# print(s1.dept.college.est_date)   #2022-12-23


#Addition
# College.objects.create(name="MIT", adr="kothrud")

# c1 = College.objects.get(id=3)           #MIT
# p1 = Principal(name="ABC", exp=20, qual="PHD", college=c1)      #as it is pass objects of college
# p1.save()

# p1 = Principal(name="ABC", exp=20, qual="PHD",college_id=3)      #as it is pass objects of college
# p1.save()

# make sure that college id is present in table
# c1 = College.objects.get(id=3)           #MIT
# d1 = Department.objects.create(name="Petrechemical",dept_str=80, college_id=3) #cllegeinstance(college)ya college id(college id)


# exec(open(r'D:\Ashwini.doc\Django_env\first_project\app1\db_shell.py').read())
# Student.objects.create(name="A",mark=44,age=18) #dept_id ya dept(dept object)
# Student.objects.create(name="B",mark=97,age=17)
# Student.objects.create(name="C",mark=49,age=19)

# fethch student by id
# s1, s2, s3 = Student.objects.filter(id__gt=9)
# print(s1,s2,s3)

# s1, s2, s3 = Student.objects.filter(id__gt=9)

# petr_dept = Department.objects.get(id=4)
# print(dir(petr_dept.studs))
# petr_dept.studs.add(s2)                 #add student in department #many to many

#--------------------------------------------------------------------------------------------------------------------------------
# # exec(open(r'D:\Ashwini.doc\Django_env\first_project\app1\db_shell.py').read())
# studs = Student.objects.all()
# print(studs)
# studs = Student.objects.all()[0]
# print(studs)

# studs = Student.objects.all()[0:7]
# print(studs)

# selected related
# studs = Student.objects.all()
# for stud in studs:
#     print(stud.dept)

# studs = Student.objects.select_related('dept')
# for stud in studs:
#     print(stud.dept)
# -------------------------------------------------------------------------------------
# many to many-------b9_db schema-----
# exec(open(r'D:\Ashwini.doc\Django_env\first_project\app1\db_shell.py').read())

# create CarModel in database table
# c180 = CarModel.objects.create(name="C180")
# c200 = CarModel.objects.create(name="C200")
# print(CarModel.objects.all())

# gas = FuleType.objects.create(name="Gas")
# diesel = FuleType.objects.create(name="Diesel")
# hybrid = FuleType.objects.create(name="Hybrid")
# print(FuleType.objects.all())
#---------------------------------------------------------------
# add 3 fuletype
# c180 = CarModel.objects.get(name="C180")

# gas = FuleType.objects.get(name="Gas")
# diesel = FuleType.objects.get(name="Diesel")
# hybrid = FuleType.objects.get(name="Hybrid")

# c180.fuletype.add(gas)
# c180.fuletype.add(diesel,hybrid)

# print(c180.fuletype.all())      #add and get
#-------------------------------------------------------------------------
# c200 = CarModel.objects.get(name="C200")

# gas = FuleType.objects.get(name="Gas")
# diesel = FuleType.objects.get(name="Diesel")
# hybrid = FuleType.objects.get(name="Hybrid")

# # c200.fuletype.add(gas)
# print(c200.fuletype.all())

# fuletype create and assign carmodel
# c200 = CarModel.objects.get(name="C200")
# c200.fuletype.create(name="Bio Diesel")

# print(c200.fuletype.all())

#------------------------------------------------------------------------------------------
# gas = FuleType.objects.get(name="Gas")
# diesel = FuleType.objects.get(name="Diesel")
# hybrid = FuleType.objects.get(name="Hybrid")
# c200 = CarModel.objects.get(name="C200")


# print(gas.carmodel_set.all())
# print(diesel.carmodel_set.all())
# print(FuleType.objects.get(name="Gas").carmodel_set.all())------------

# releted_name diya hai vhi use karo-------------------
# print(gas.carmodels.all())

# print(CarModel.objects.filter(fuletype__name__startswith="G"))
# print(CarModel.objects.filter(fuletype__name__startswith="D"))

# print(FuleType.objects.filter(carmodels__name__startswith="C"))

# print(FuleType.objects.filter(carmodels__name="C180"))
# print(FuleType.objects.filter(carmodels__name="C200"))  

# print(FuleType.objects.filter(carmodels__name__startswith="C").distinct())   #distinct se repeat nhi hoga

#----------------------------------------------------------
# exec(open(r'D:\Ashwini.doc\Django_env\first_project\app1\db_shell.py').read())

# create connection with pymysql 
# raw sql query
# 1st way
# from django.db import connection
# cursor = connection.cursor()
# cursor.execute('''SELECT * FROM student''')
# data = cursor.fetchall()
# data = cursor.fetchmany(4)
# again hit same query print next 3 records
# data = cursor.fetchmany(3)
# print(data)


# 2nd way to fatch all data
# data = Student.objects.raw("SELECT * FROM student")
# for i in data:
#     print(i)



#--------------------------------
# MUltiple  Database
# MySQL, SQLite
# exec(open(r'D:\Ashwini.doc\Django_env\first_project\app1\db_shell.py').read())

# data = Student.objects.all()
# print(data)

SECOND_DATABASE = "Second_db"
# data = Student.objects.using(SECOND_DATABASE).all()
# print(data)

# c1 = College.objects.using(SECOND_DATABASE).create(name="COPT", adr="Pune")
# d1 = Department.objects.using(SECOND_DATABASE).create(name="ENTC", dept_str=60, college=c1)

# d1 = Department.objects.get(id=1)
# s1 = Student.objects.using(SECOND_DATABASE).create(name="XYZ", mark=89, age=25, dept=d1)
# s2 = Student.objects.using(SECOND_DATABASE).create(name="PQR", mark=95, age=26, dept=d1)
# subj1 = Subjects.objects.using(SECOND_DATABASE).create(name="Data Signal", is_practical=True, dept=d1)

# studs = Student.objects.using(SECOND_DATABASE).all()
# print(studs)