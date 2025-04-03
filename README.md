# Codebar: Web Development Workshops

## About the Project

Codebar is a web development school offering workshops for students and instructors. This project allows you to manage members (students and instructors) and organize workshops, providing a simple and effective way to handle participants and workshop details. 

!!! The task comes from github: https://github.com/nrorabaugh/python-oop-exercise

---

## Features 

- **Member Management**:
  - Students have a reason for attending Codebar.
  - Instructors have a biography and skills, which can be updated dynamically.
- **Workshop Management**:
  - Includes date, subject, list of instructors, and students.
  - Add participants dynamically based on their role (Student or Instructor).
  - Display detailed information about each workshop.

---

## Technologies Used

- **Language**: Python
- **Libraries**: None (pure Python implementation)

---

## Getting Started

### Prerequisites

- Python 3.8 or higher installed on your system.

### Installation

1. Clone the repository:
git clone: https://github.com/astepni/Codebar-Web-Development-Workshops

2. Navigate to the project directory:
cd codebar


### Running the Project

1. Create members (students and instructors):

from codebar import Student, Instructor, Workshop

student1 = Student("Anna Kowalska", "I always wanted to create websites!")
instructor1 = Instructor("Jan Nowak", "I've been coding in Python for 5 years and want to share this love!")
instructor1.add_skill("Python")
instructor1.add_skill("JavaScript")

2. Create a workshop and add participants:

workshop = Workshop("2025-04-03", "Web Development Basics")
workshop.add_participant(student1)
workshop.add_participant(instructor1)


3. Display workshop details:
workshop.print_details()
