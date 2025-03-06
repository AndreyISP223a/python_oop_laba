class Department:
  department = None

  def __init__(self,department):
    self.department = department

class Position:
  position = None

  def __init__(self,position):
    self.position = position
    
class User :
  name = None
  position = None
  department = None

  def __init__(self,name, position, department):
    self.name = name
    self.position = position
    self.department = department
    
department = Department('Police')
position = Position('Recruit')
user = User('John', position, department)

print (user.name)
print (user.department.department)
print (user.position.position)
