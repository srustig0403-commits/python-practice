# File Name: employee_dictionary.py

# Employee Dictionary Program

employee = {
    "id": 101,
    "name": "Rahul",
    "department": "IT",
    "salary": 25000
}

# Display employee details
print("Employee Details")
print(employee)

# Access specific values
print("\nEmployee Name:", employee["name"])
print("Department:", employee["department"])

# Add new key-value pair
employee["city"] = "Bangalore"

# Update salary
employee["salary"] = 30000

# Display updated dictionary
print("\nUpdated Employee Details")
print(employee)

# Remove department
del employee["department"]

# Final dictionary
print("\nFinal Dictionary")
print(employee)
