from django.db import models

# # Create your models here.
# # ORM -- Oject Relational Mapper
# #active class defined for person
class ActivePerson(models.Manager):  #Custom Model manager
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)   #Model.objects.all()

class InActivePerson(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)

class Person(models.Model): #table #app_person
    
    # default id
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    date_joined = models.DateTimeField(auto_now=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    activep = ActivePerson()
    inactivep = InActivePerson()
    # all_data = models.Manager()     #objects
    objects = models.Manager()         #object


    class Meta:
        db_table = "person"

    def __str__(self):
        # return self.name
        return f"{self.name} -- {self.address}"

    def show_details(self):
        print(f"""-------------------------------------
Person Name:- {self.name}
Person Age:- {self.age}
Person Mobile:-{self.mobile_no}
Person Address:-{self.address}""")

    @classmethod
    def get_data_above_age(cls):
        return cls.objects.filter(age__gte=25)      #gt ,gte, lt, lte, startswith , endswith

    @classmethod
    def get_avg_age(cls):
        '''avarage age of all persons'''
        Data = cls.objects.all().values("id", "name", "age")
        lst = (list(map(lambda x: x['age'],list(Data))))
        return sum(lst)//len(lst)
    # method for active data
    @classmethod
    def get_active_data(cls):
        return cls.objects.filter(is_active=True)
    #method for inactive data
    @classmethod
    def get_inactive_data(cls):
        return cls.objects.filter(is_active=False)


#------------------------------------------------------------------------------relationship        

class CommonClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True



class College(CommonClass):
    adr = models.CharField(max_length=500)
    est_date = models.DateField(auto_now=True)
    class Meta:
        db_table = "college"

class Principal(CommonClass):
    exp = models.FloatField()
    qual = models.CharField(max_length=50)
    college = models.OneToOneField(College, on_delete=models.CASCADE, related_name='princi')
    class Meta:
        db_table = "principal"


class Department(CommonClass):
    dept_str = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='depts')        #OneToMany Field
    class Meta:
        db_table = "dept"
        # unique_together = (("name", "college"))



class Student(CommonClass):
    mark = models.IntegerField()
    age = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='studs',null=True)                 #OneToMany Field
    class Meta:
        db_table = "student"

      
class Subjects(CommonClass):
    is_practical = models.BooleanField(default=True)
    student = models.ManyToManyField(Student)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjs')
    class Meta:
        db_table = "subject"

# ERD Diagram -entity relationship diagram



##-------------------------------------------------------------------

##b9_db

# class FuleType(models.Model):
#     name = models.CharField(max_length=255)
#     class Meta:
#         db_table = "fuletype"

#     def __str__(self):
#         return f"{self.name}"

# class CarModel(models.Model):
#     name = models.CharField(max_length=255)
#     fuletype = models.ManyToManyField(FuleType, related_name='carmodels')
#     class Meta:
#         db_table = "carmodel"
    
#     def __str__(self):
#         return f"{self.name}"