class Employee:
  __name = None

  def __init__(self,name):
    self.__name = name

  def getName(self):
    return self.__name
    
employees = [
        Employee('Sam'),
        Employee('Marie'),
        Employee('Bob'),
        Employee('John')
]
for emp in employees:
	print(emp.getName()) 
