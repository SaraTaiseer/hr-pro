from datetime import datetime
class Employee:
        def __init__ (self,name,age,salary ,employment_year):
                self.name =name
                self.age=age
                self.salary=salary
                self.employment_year=employment_year
        def get_working_years(self):
                y=datetime.now().year -self.employment_year
                return y
        def __str__ (self):
                return "Name: "+self.name+", Age: "+str(self.age)+", Salary: "+str(self.salary)+", Working Years: "+str(self.get_working_years())
        
                
                
   #Employee class here

class Manager(Employee):
        def __init__ (self,name,age,salary ,employment_year,bonus_percentage):
                Employee.__init__(self,name,age,salary ,employment_year)
                self.bonus_percentage = bonus_percentage
        def get_bonus(self):
                return self.bonus_percentage* self.salary
        def __str__(self):
                return Employee.__str__(self)+", Bonus: "+str(self.get_bonus)
                
        
    #Manager class here

        
def main():
        Employees=[]
        Managers=[]
        print("Welcome to HR Pro 2019")
        num=1
        while num>0 and num<5:
                
                print("Options:")
                print("    1. Show Employees ")
                print("    2. Show Managers ")
                print("    3. Add An Employee ")
                print("    4. Add A Manager ")
                print("    5. Exit ")
                print()
                num =int(input("What would you like to do?"))
                print("---------------------")
                
                if num ==1:
                        for n in Employees:
                                print (n)
                elif num ==2:
                        for n in Managers:
                                print (n)
                elif num ==3:
                        name_e=input("Name: ")
                        age_e=int(input("Age: "))
                        salary_e=int(input("Salary: "))
                        emp_year_e=int(input("Employement year: "))
                        e=Employee(name_e,age_e,salary_e,emp_year_e)
                        Employees.append(e)
                        print("Employee addes succesfuly")
                elif num == 4:
                        name_m=input("Name: ")
                        age_m=int(input("Age: "))
                        salary_m=int(input("Salary: "))
                        emp_year_m=int(input("Employement year: "))
                        bonus=float(input("Bonus Percentage:" ))
                        m=Manager(name_m,age_m,salary_m,emp_year_m,bonus)
                        Managers.append(m)
                        print("Manager addes succesfuly")
                        

             
       
        # main code here

if __name__ == '__main__':
        main()
