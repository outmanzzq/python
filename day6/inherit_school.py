# author: zzq


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self, stu_obj):
        print("为学员%s 办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        print("雇佣新员工%s" % staff_obj.name)
        self.staffs.append(staff_obj)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---- info of Teacher: %s ----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Sex:%s
        '''%(self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s is teaching course [%s]" %(self.name, self.course))


class Students(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Students, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
                ---- info of Teacher: %s ----
                Name:%s
                Age:%s
                Sex:%s
                Salary:%s
                Sex:%s
                ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self, amount):
        print("%s has paid tution for $%s" %(self.name, amount))


school = School("老男孩IT", "沙河")

t1 = Teacher("Oldboy", 56, "MF", 2000000, "Linux")
t2 = Teacher("Oldboy", 22, "M", 3000, "PythobDevOps")

s1 = Students("ChenRonghua", 36, "MF", 1001, "PythobDevOps")
s2 = Students("徐良伟", 19, "F", 1002, "Linux")

t1.tell()
s1.tell()

school.enroll(s1)
school.enroll(s2)
school.hire(t1)

print(school.students)
print(school.staffs)
school.staffs[0].teach()

for stu in school.students:
    stu.pay_tuition(5000)
