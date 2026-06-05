from datetime import datetime


def add_students():
    n = int(input("How many students do you want to add? "))

    existing_students = []

    try:
        with open("students.txt", "r") as file:
            existing_students = [line.strip().lower() for line in file]
    except FileNotFoundError:
        pass

    with open("students.txt", "a") as file:
        for i in range(n):
            name = input(f"Enter student {i+1} name: ")

            if name.lower() in existing_students:
                print(f"{name} already exists!")
            else:
                file.write(name + "\n")
                existing_students.append(name.lower())
                print(f"{name} added successfully!")

    print("\nStudent addition process completed!")

def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if len(students) == 0:
            print("\nNo students found.")

        else:
            print("\n===== Student List =====")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student.strip()}")

    except FileNotFoundError:
        print("\nNo student records found.")


def mark_attendance():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if len(students) == 0:
            print("\nNo students available.")
            return

        date = datetime.now().strftime("%d-%m-%Y")

        with open("attendance.txt", "a") as att_file:
            att_file.write(f"\nDate: {date}\n")

            print(f"\n===== Attendance for {date} =====")

            for student in students:
                name = student.strip()

                while True:
                    status = input(f"{name} (P/A): ").upper()

                    if status in ["P", "A"]:
                        break

                    print("Please enter only P or A.")

                att_file.write(f"{name} - {status}\n")

        print("\nAttendance marked successfully!")

    except FileNotFoundError:
        print("\nNo students found. Add students first.")

def view_attendance():
    try:
        with open("attendance.txt", "r") as file:
            records = file.read()

        if records.strip() == "":
            print("\nNo attendance records found.")

        else:
            print("\n===== Attendance Report =====")
            print(records)

    except FileNotFoundError:
        print("\nNo attendance records found.")

def attendance_percentage():
    try:
        with open("attendance.txt", "r") as file:
            lines = file.readlines()

        attendance = {}

        for line in lines:
            line = line.strip()

            if line.startswith("Date:") or line == "":
                continue

            name, status = line.split(" - ")

            if name not in attendance:
                attendance[name] = {"present": 0, "total": 0}

            attendance[name]["total"] += 1

            if status == "P":
                attendance[name]["present"] += 1

        print("\n===== Attendance Percentage =====")

        for name, data in attendance.items():
            percentage = (data["present"] / data["total"]) * 100
            print(f"{name} : {percentage:.2f}%")

    except FileNotFoundError:
        print("\nNo attendance records found.")

def search_student():
    try:
        name_to_search = input("Enter student name to search: ").strip()

        with open("students.txt", "r") as file:
            students = [line.strip() for line in file]

        if name_to_search in students:
            print(f"\n{name_to_search} found in student list.")

            try:
                with open("attendance.txt", "r") as att_file:
                    lines = att_file.readlines()

                present = 0
                total = 0

                for line in lines:
                    line = line.strip()

                    if line.startswith(name_to_search + " - "):
                        total += 1

                        if line.endswith("P"):
                            present += 1

                if total > 0:
                    percentage = (present / total) * 100
                    print(f"Attendance Percentage: {percentage:.2f}%")
                else:
                    print("No attendance records found.")

            except FileNotFoundError:
                print("Attendance file not found.")

        else:
            print(f"\n{name_to_search} not found.")

    except FileNotFoundError:
        print("Student file not found.")

while True:
    print("\n===== Attendance Management System =====")
    print("1. Add Students")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Attendance Percentage")
    print("6. Search Student")
    print("7. Exit")


    choice = input("Enter your choice: ")

    if choice == "1":
        add_students()

    elif choice == "2":
        view_students()

    elif choice == "3":
        mark_attendance()

    elif choice == "4":
        view_attendance()

    elif choice == "5":
        attendance_percentage()

    elif choice == "6":
        search_student()

    elif choice == "7":
        print("\nThank you for using the Attendance Management System!")
        break

    else:
        print("\nInvalid choice! Please try again.")