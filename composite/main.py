from abc import ABCMeta, abstractmethod

class DepartmentInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *args):
        pass

    @abstractmethod
    def showDetails():
        pass

class ChildDepartment(DepartmentInterface):
    def __init__(self, *args):  
        self.position = args[0]
  
    def showDetails(self):
        print("\t", end ="")
        print(self.position)

class ParentDepartment(DepartmentInterface):
    def __init__(self, *args):
        self.position = args[0]
        self.children = []
  
    def add(self, child):
        self.children.append(child)
  
    def remove(self, child):
        self.children.remove(child)
  
    def showDetails(self):
        print(self.position)
        for child in self.children:
            print("\t", end ="")
            child.showDetails()



if __name__ == "__main__":
  
    development_dept= ParentDepartment("Development Department")
    web_dev_dept = ParentDepartment("Web Development Department")
    qa_dept = ParentDepartment("QA Department")
    backend_dept = ChildDepartment("Back-End Dept")
    frontend_dept = ChildDepartment("Front-End Dept")
    testing_dept = ChildDepartment("Testing Dept")
    
    web_dev_dept.add(backend_dept)
    web_dev_dept.add(frontend_dept)
    qa_dept.add(testing_dept)
    development_dept.add(qa_dept)
    development_dept.add(web_dev_dept)
    development_dept.showDetails()