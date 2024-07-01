# class employee:
#     num_of_emps=0
#     raise_amount=1.04


#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+'.'+last+'@company.com'

#         employee.num_of_emps +=1

#     def fullname(self):
#         return'{} {}'.format(self.first,self.last)
    
#     def applyraise(self):
#          self.pay=int(self.pay * self.raise_amount)


#     # print(employee.num_of_emps)
# emp_1=employee('aman','patel',29000)
# emp_2=employee('alfiya','patel',24000)
# # print(emp_1.email)
# # print(emp_2.email)
# # print('{},{}'.format(emp_1.first,emp_1.last))
# # print(emp_1.fullname())
# # print(employee.fullname(emp_1))
# # print(emp_1.pay)
# # emp_1.applyraise()
# # print(emp_1.pay)
# # employee.raise_amount=1.05

# #CLASS VARIABLES AND INSTANCE VARIABLES

# # emp_1.raise_amount=1.05 #if we change the attribute using the class itself then it will change in all the instances and if we change the class variables using instances then it will change the variable in only that instance
# print(emp_1.__dict__)
# print(emp_2.__dict__)
# # # employee.raise_amount
# print(employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# # #we can access this class variables from all instances and all classes
# # print(emp_1.__dict__)

# emp_1.applyraise()
# print(emp_1.pay)
# print(employee.num_of_emps)







# # REGULAR METHODS , CLASS METHODS AND STATIC METHODS

# # A REGULAR METHOD AUTOMATICALLY TAKES IN THE INSTANCE AS THE FIRST ARGUMENT WHICH IS 'SELF'
# # TO CONVERT A REGULAR METHOD INTO A CLASS METHOD WE JUST NEED TO GIVE A @CLASSMETHOD DECORATOR


# class employee:

#     num_of_emps=0
#     raise_amt=1.04

#     def __init__(self,first,last,pay):
#       self.first=first
#       self.last=last
#       self.pay=pay
#       self.email=first+'.'+last+'@company.com'

#       employee.num_of_emps+=1

#     def fullname(self):
#          return '{} {}'.format(self.first,self.last)
      
#     def apply_raise(self):
#          self.pay= int(self.pay*self.raise_amt)

#     @classmethod
#     def set_raise_amt(cls,amount):
#          cls.raise_amt=amount
#     @classmethod
#     def from_string(cls,emp_str):
#         first,last,pay=emp_str.split('-')
#         return cls(first,last,pay)
#     @staticmethod
#     def is_work_day(day):
#         if day.weekday()==5 or day.weekday()==6:
#             return False
#         return True

# emp_1=employee('aman','patel',29000)
# emp_2=employee('alfiya','patel',24000)


# import datetime
# my_date=datetime.date(2016,7,10)
# print(employee.is_work_day(my_date))
# employee.set_raise_amt(1.05)

# print(employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# class methods as alternative constructors


# emp_str_1='john-doe-39000'
# emp_str_2='steve-smith-30000'
# emp_str_3='jane-doe-70000'

# # first,last,pay=emp_str_1.split('-')

# # new_emp_1=employee(first,last,pay)

# new_emp_1=employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)






# inheritance

# class employee:
#     num_of_emps=0
#     raise_amount=1.04


#     def __init__(self,first,last,pay):
#          self.first=first
#          self.last=last
#          self.pay=pay
#          self.email=first+'.'+last+'@company.com'

#          employee.num_of_emps +=1

#     def fullname(self):
#          return'{} {}'.format(self.first,self.last)
    
#     def applyraise(self):
#          self.pay=int(self.pay * self.raise_amount)


# class developer(employee):
#      raise_amount=1.10
#      def __init__(self, first, last, pay,prog_lang):
#           super().__init__(first,last,pay)
#           self.prog_lang=prog_lang

# class manager(employee):
#      def __init__(self, first, last, pay,employees=None):
#           super().__init__(first, last, pay)
#           if employees is None:
#                self.employees=[]
#           else:
#                self.employees=employees

#      def add_emp(self,emp):
#           if emp not in self.employees:
#                self.employees.append(emp)
#      def remove_emp(self,emp):
#           if emp in self.employees:
#                self.employees.remove(emp)   

#      def print_emps(self):
#           for emp in self.employees:
#                print('-->', emp.fullname())  



               
#         #   employee.__init__(self,first,last,pay)
# # dev_1=employee('aman','patel',20000)
# # dev_2=employee('alfiya','patel',20000)
# # THIS CHAIN IS CALLED THE METHOD RESOLUTION ORDER

# dev_1=developer('aman','patel',20000,'java')
# dev_2=developer('alfiya','patel',20000,'python')

# mgr_1=manager('joe','root',80000,[dev_1])
# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_2)
# mgr_1.print_emps()
# # print(help(developer)) 

# # print(dev_1.email)
# # print(dev_2.prog_lang)

# # print(dev_1.pay)
# # dev_1.applyraise()
# # print(dev_1.pay)

# print(isinstance(mgr_1,manager))
# print(issubclass(developer,employee))




# special methods or magic  methods
class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
         if isinstance(other, Employee):
            return self.pay + other.pay
            return NotImplemented
         
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Aman', 'Patel', 20000)
emp_2 = Employee('Alfiye', 'Patel', 20000)

# Using repr and str
print(repr(emp_1))
print(str(emp_1))

# Using magic methods explicitly
print(emp_1.__repr__())
print(emp_1.__str__())

# Correctly adding the salaries
print(emp_1+emp_2)
print(len('test'))
print('test'.__len__())
print(len(emp_1))






 