students = ["Amit", "Riya", "Karan", "Sneha"]
print("Initial student list:", students)

# 1. append() – Add a new student
students.append("Rahul")
print("After append:", students)

# 2. insert() – Insert a student at position
students.insert(1, "Priya")
print("After insert:", students)

# 3. remove() – Remove a student
students.remove("Karan")
print("After remove:", students)

# 4. pop() – Remove last student
students.pop()
print("After pop:", students)

# 5. sort() – Arrange names alphabetically
students.sort()
print("After sort:", students)

# 6. reverse() – Reverse the list
students.reverse()
print("After reverse:", students)

# 7. len() – Total number of students
print("Total students:", len(students))

# 8. count() – Count a student name
students.append("Amit")
print("Amit appears:", students.count("Amit"), "times")

# 9. index() – Find position of a student
print("Index of Riya:", students.index("Riya"))

# 10. extend() – Add another list of students
new_students = ["Neha", "Arjun"]
students.extend(new_students)
print("Final student list:", students)