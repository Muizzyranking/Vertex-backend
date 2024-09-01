# Assignment: Build a Simple School Management System

## For this assignment, you will apply your Object-Oriented Programming (OOP) knowledge alongside the concepts learned so far to build a School Management System. This system will manage students, teachers, courses, and grades. The assignment is divided into several steps to guide you through the process.

## Objectives:

- Apply OOP concepts in a practical project.
- Gain experience in designing and implementing classes and their interactions.
- Develop skills in problem-solving and project management.

## step-by-step guide:

### step 1: plan your classes

  - Identify the classes:
    - `Student`: represents a student with attributes like name, id, age, and enrolled courses.
    - `Teacher`: represents a teacher with attributes like name, id, subject, and assigned courses.
    - `Course`: represents a course with attributes like course name, course code, and enrolled students.
    - `School`: represents the school itself, managing all students, teachers, and courses.
  - define relationships:
    - a student can enroll in multiple courses.
    - a teacher can teach multiple courses.
    - a course can have multiple students and one teacher.

### step 2: create the classes
  - Define the student class:
    - attributes: `name`, `student_id`, `age`, `courses` (a list to store enrolled courses).
    - methods:
      - `enroll(course)`: enrolls the student in a course.
      - `view_courses()`: displays the courses the student is enrolled in.
  - Define the teacher class:
    - attributes: `name`, `teacher_id`, `subject`, `courses` (a list to store courses taught by the teacher). 
    - methods: - `assign_course(course)`: assigns a course to the teacher. - `view_courses()`: displays the courses the teacher is teaching.
  - Define the course class:
    - attributes: `course_name`, `course_code`, `teacher` (a reference to the teacher), students (a list to store enrolled students).
    - methods:
      - `add_student(student)`: adds a student to the course.
      - `view_students()`: displays the students enrolled in the course.

- Define the school class:
- attributes: name, students (a list to store all students), teachers (a list to store all teachers), courses (a list to store all courses).
- methods:
  - `add_student(student)`: adds a student to the school.
  - `add_teacher(teacher)`: adds a teacher to the school.
  - `add_course(course)`: adds a course to the school.
  - `view_all_students()`: displays all students in the school.
  - `view_all_teachers()`: displays all teachers in the school.
  - `view_all_courses()`: displays all courses in the school.
### step 3: implement basic operations
1. Adding and viewing students:
   - implement the logic to add students to the school and view all students.

2. Assigning teachers to courses:
    - implement the logic to assign teachers to courses and view the courses they teach.
3. Enrolling students in courses:
    - implement the logic for enrolling students in courses and viewing their enrolled courses.

### step 4: enhance the system with advanced features (optional)
1. Track grades:
    - add functionality to track student grades in each course.
    - update the course class to include methods like `assign_grade(student, grade)` and `view_grades()`.
2. Generate reports:
    - add methods to generate reports, such as a student’s grade report or a teacher’s course report.
3. Implement user interaction:
    - add a simple text-based menu system that allows users to interact with the system, like adding students, enrolling in courses, viewing grades, etc.

### step 5: test your system
1. Create sample data:
    - create a few students, teachers, and courses.
    - simulate interactions, such as enrolling students in courses and assigning grades.
2. Test all scenarios:
    - test the system to ensure that all methods work correctly.
    - handle any errors or edge cases, such as enrolling a student in a course more than once.

### step 6: documentation and submission
Document your code:
    - write comments explaining each class, method, and their purposes.
Submit your assignment:
    - Submit your assignment on github

