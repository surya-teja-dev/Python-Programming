student = {
    "name": "Surya Teja",
    "course": "CSE-AIML",
    "language": "Python"
}
print("Student details:", student)
print("Name:", student["name"])
student["year"] = 2
print("After adding year:", student)
for key, value in student.items():
    print(key, ":", value)
