class Student:
    def __init__(self, sid, deptid):
        self.sid = sid
        self.deptid = deptid
    def get_info(self):
        return f"StudentID: {self.sid}, DepartmentID: {self.deptid}"
class Faculty:
    def __init__(self, eid, deptid):
        self.eid = eid
        self.deptid = deptid
    def get_info(self):
        return f"FacultyID: {self.eid}, DepartmentID: {self.deptid}"
class PhDStudent(Student, Faculty):
    def __init__(self, sid, eid, deptid):
        Student.__init__(self, sid, deptid)
        Faculty.__init__(self, eid, deptid)
    def get_info(self):
        return f"StudentID: {self.sid}, EmployeeID: {self.eid}, DepartmentID: {self.deptid}"
obj1 = Student(1, 101)
obj2 = Faculty(23, 101)
obj3 = PhDStudent(1, 23, 101)
print(obj1.get_info())
print(obj2.get_info())
print(obj3.get_info())
