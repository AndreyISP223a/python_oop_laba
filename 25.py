# еще не сделано
class Employee:
  __name = None

  def __init__(self,name):
    self.__name = name

  def getName(self):
    return self.__name

class EmployeesCollection:
    def __init__(self):
        self.__users = []

    def add(self,user):
        self.__users.append(user)
