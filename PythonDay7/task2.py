class Employee:
    def __init__(self, empname, empid, job, salary, dept):
        self.empname = empname
        self.empid = empid
        self.job = job
        self.salary = salary
        self.dept = dept
    def emp_details(self):
        print("Employee Name :", self.empname)
        print("Employee ID   :", self.empid)
        print("Job           :", self.job)
        print("Salary        :", self.salary)
        print("Department    :", self.dept)
        print("-" * 30)
e1 = Employee("Rahul", 101, "Manager", 70000, "HR")
e2 = Employee("Priya", 102, "Developer", 60000, "IT")
e3 = Employee("Arjun", 103, "Tester", 45000, "QA")
e4 = Employee("Sneha", 104, "Analyst", 55000, "Finance")
e5 = Employee("Kiran", 105, "Developer", 62000, "IT")
e1.emp_details()
e2.emp_details()
e3.emp_details()
e4.emp_details()
e5.emp_details()
