# File Name: dictionary_demo.py

# Dictionary Example

student = {
    "name": "Nandan",
    "age": 16,
    "course": "Python"
}

# Print dictionary
print("Student Details:")
print(student)

# Access values
print("Name:", student["name"])
print("Age:", student["age"])

# Add new item
student["grade"] = "A"

# Update value
student["age"] = 17

# Print updated dictionary
print("\nUpdated Dictionary:")
print(student)

# Remove item
student.pop("course")

print("\nAfter Removing Course:")
print(student)
