# class Student:
#     def __init__(self, student_id, student_name, student_marks):
#         self.id = student_id
#         self.name = student_name
#         if 0 <= student_marks <= 100:
#             self.marks = student_marks
#         else:
#             self.marks = None
#             print("Invalid Marks")
#     def display_details(self):
#         print("\n========== Student Details ==========")
#         print(f"Student ID: {self.id}")
#         print(f"Student Name: {self.name}")
#         if self.marks is not None:
#             print(f"Student Marks: {self.marks}")
#             print(f"Grade: {self.calculate_grade()}")
#     def calculate_grade(self):
#         if self.marks >= 90:
#             return "A"
#         elif self.marks >= 75:
#             return "B"
#         elif self.marks >= 60:
#             return "C"
#         elif self.marks >= 40:
#             return "D"
#         else:
#             return "Fail"
# S1 = Student(1, "Nivedith", 95)
# S2 = Student(2, "Pavan", 26)
# S3 = Student(3, "Sai", 72)
# S4 = Student(4, "Rahul", 100)
# S1.display_details()
# S2.display_details()
# S3.display_details()
# S4.display_details()