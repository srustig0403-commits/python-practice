# File Name: smart_hospital_data_management_system.py

print("===== SMART HOSPITAL DATA MANAGEMENT SYSTEM =====")

# Dictionary
patients = {}

# Stack
reports = []

# Queue
queue = []

while True:

    print("\n1.Add Patient")
    print("2.View Patients")
    print("3.Push Report")
    print("4.Pop Report")
    print("5.Enqueue Patient")
    print("6.Dequeue Patient")
    print("7.Number Conversion")
    print("8.Exit")

    choice = input("Enter Choice: ")

    # Add Patient
    if choice == "1":
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")

        patients[pid] = name

        print("Patient Added Successfully")

    # View Patients
    elif choice == "2":

        print("\nPatient Records")

        for pid, name in patients.items():
            print(pid, ":", name)

    # Push Report
    elif choice == "3":

        report = input("Enter Report Name: ")
        reports.append(report)

        print("Report Added")

    # Pop Report
    elif choice == "4":

        if len(reports) == 0:
            print("No Reports")
        else:
            print("Removed Report:", reports.pop())

    # Enqueue Patient
    elif choice == "5":

        patient = input("Enter Emergency Patient Name: ")
        queue.append(patient)

        print("Patient Added to Queue")

    # Dequeue Patient
    elif choice == "6":

        if len(queue) == 0:
            print("Queue Empty")
        else:
            print("Treated Patient:", queue.pop(0))

    # Number Conversion
    elif choice == "7":

        num = int(input("Enter Decimal Number: "))

        print("Binary:", bin(num))
        print("Octal:", oct(num))
        print("Hexadecimal:", hex(num))

    # Exit
    elif choice == "8":

        print("Thank You")
        break

    else:
        print("Invalid Choice")
