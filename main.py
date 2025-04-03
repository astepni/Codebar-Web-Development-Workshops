
class Member: 
    def __init__(self, full_name):
        self.full_name = full_name

    def introduce(self):
        return f"Cześć, nazywam się {self.full_name}!"

class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason

class Instructor(Member):
    def __init__(self, full_name, bio):
        super().__init__(full_name)
        self.bio = bio
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, member):
        if isinstance(member, Instructor):
            self.instructors.append(member)
        elif isinstance(member, Student):
            self.students.append(member)

    def print_details(self):
        print(f"Warsztat: {self.subject}")
        print(f"Data: {self.date}")
        print("Instruktorzy:")
        for instructor in self.instructors:
            print(f"- {instructor.full_name} (Bio: {instructor.bio}, Umiejętności: {', '.join(instructor.skills)})")
        print("Studenci:")
        for student in self.students:
            print(f"- {student.full_name} (Powód: {student.reason})")

student1 = Student("Anna Kowalska", "Zawsze chciałam tworzyć strony internetowe!")
instructor1 = Instructor("Jan Nowak", "Koduję w Pythonie od 5 lat i chcę podzielić się tą miłością!")
instructor1.add_skill("Python")
instructor1.add_skill("JavaScript")

workshop = Workshop("2025-04-03", "Tworzenie stron internetowych")
workshop.add_participant(student1)
workshop.add_participant(instructor1)

workshop.print_details()
