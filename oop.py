class Assignment:
    def __init__(self, name: str, difficulty: float):
        self.name = name
        self.difficulty = difficulty
        
    def get_name(self):
        return self.name
        
    def get_difficulty(self):
        return self.difficulty
    
    def __str__(self):
        return self.name
        

class AssignmentResult:
    def __init__(self, id:int, assignment, grade: float):
        self.id = id
        self.assignment = assignment
        self.grade = grade
        
    def get_id(self):
        return self.id
    
    def get_grade(self):
        return self.grade
    
    def get_assignment(self):
        return self.assignment


class Student:
    def __init__(self, id: int, fist_name: str, last_name: str, town:str):
        self.id = id
        self.fist_name = fist_name
        self.last_name = last_name
        self.town = town
        self.energy = 1.0
        self.grade = 0
        self.frst = None
    
    def get_id(self):
        return self.id
    
    def get_first_name(self):
        return self.fist_name
        
    def set_first_name(self, name:str):
        self.fist_name = name
        
    def get_last_name(self):
        return self.last_name
        
    def set_last_name(self, name: str):
        self.last_name = last_name
        
    def get_town(self):
        return self.town
    
    def set_town(self, town: str):
        self.town = town
        
    def __str__(self):
        return (self.fist_name+" "+self.last_name)
    
    def get_grade(self):
        return self.grade
    
    def assign(self, assignment):
        diff = assignment.get_difficulty()
        if diff > 1:
            diff = assignment.get_difficulty()/100
            
        self.grade = 1 - (self.energy * diff)
        self.energy = (self.energy - (self.energy * diff))
        
        if self.energy < 0:
            self.energy = 0
            
        if self.frst == None:
            self.frst = self.grade
        
        return AssignmentResult(self.id, assignment, self.grade)
        
    def sleep(self, hours:float):
        self.energy = (self.energy * (1 + (hours/10)))
        if self.energy > 1:
            self.energy = 1.0
        
    def get_energy(self):
        return self.energy
    
class Course:
    def __init__(self, students: list):
        self.students = students
    
    def get_mean_grade(self):
        grades = []
        for student in self.students:
            grades.append(student.get_grade())
        return (sum(grades)/(len(self.students)))
        
    def get_max_grade(self):
        grades = []
        for student in self.students:
            grades.append(student.get_grade())
        return max(grades)
    
    def get_min_grade(self):
        grades = []
        for student in self.students:
            grades.append(student.get_grade())
        return min(grades)
        
    def get_median_grade(self):
        from statistics import median
        
        grades = []
        for student in self.students:
            grades.append(student.get_grade())
        
        return median(grades)

    def get_grade_variance(self):
        grades = []
        for student in self.students:
            grades.append(student.get_grade())
        
        avg = sum(grades) / len(grades)
        var = sum((x-avg)**2 for x in grades) / len(grades)
        return var
    
    def get_grade_std_dev(self):
        from math import sqrt
        return sqrt(self.get_grade_variance())
        
    def assign(self, name: str, difficulty: float):
        assignment = Assignment(name, difficulty)
        for student in self.students:
            student.assign(assignment)
