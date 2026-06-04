# Task 7: Student Management System
# Synent Technologies Python Internship

import json
import os

FILE = "students.json"

def load_students():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return []

def save_students(students):
    with open(FILE, 'w') as f:
        json.dump(students, f, indent=4)

def add_student(students):
    print("\n--- Add Student ---")
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    roll = input("Enter roll number: ").strip()
    if any(s['roll'] == roll for s in students):
        print(f"Roll number {roll} already exists!")
        return

    try:
        marks = float(input("Enter marks (0-100): "))
        if not (0 <= marks <= 100):
            print("Marks must be between 0 and 100!")
            return
    except ValueError:
        print("Invalid marks! Enter a number.")
        return

    branch = input("Enter branch: ").strip()

    student = {"name": name, "roll": roll, "marks": marks, "branch": branch}
    students.append(student)
    save_students(students)
    print(f"Student '{name}' added successfully!")

def view_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No students found.")
        return
    print(f"\n{'Roll':<10} {'Name':<20} {'Marks':<10} {'Branch':<15}")
    print("-" * 55)
    for s in students:
        print(f"{s['roll']:<10} {s['name']:<20} {s['marks']:<10} {s['branch']:<15}")
    print(f"\nTotal students: {len(students)}")

def update_student(students):
    print("\n--- Update Student ---")
    roll = input("Enter roll number to update: ").strip()
    for s in students:
        if s['roll'] == roll:
            print(f"Found: {s['name']} | Marks: {s['marks']} | Branch: {s['branch']}")
            new_name   = input(f"New name (press Enter to keep '{s['name']}'): ").strip()
            new_marks  = input(f"New marks (press Enter to keep '{s['marks']}'): ").strip()
            new_branch = input(f"New branch (press Enter to keep '{s['branch']}'): ").strip()

            if new_name:
                s['name'] = new_name
            if new_marks:
                try:
                    s['marks'] = float(new_marks)
                except ValueError:
                    print("Invalid marks! Keeping old value.")
            if new_branch:
                s['branch'] = new_branch

            save_students(students)
            print("Student updated successfully!")
            return
    print(f"No student found with roll number '{roll}'.")

def delete_student(students):
    print("\n--- Delete Student ---")
    roll = input("Enter roll number to delete: ").strip()
    for s in students:
        if s['roll'] == roll:
            confirm = input(f"Delete '{s['name']}'? (yes/no): ").strip().lower()
            if confirm == 'yes':
                students.remove(s)
                save_students(students)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
    print(f"No student found with roll number '{roll}'.")

def search_student(students):
    print("\n--- Search Student ---")
    keyword = input("Enter name or roll number to search: ").strip().lower()
    results = [s for s in students if keyword in s['name'].lower() or keyword in s['roll'].lower()]
    if results:
        print(f"\n{'Roll':<10} {'Name':<20} {'Marks':<10} {'Branch':<15}")
        print("-" * 55)
        for s in results:
            print(f"{s['roll']:<10} {s['name']:<20} {s['marks']:<10} {s['branch']:<15}")
    else:
        print("No matching student found.")

def main():
    print("=" * 45)
    print("  Synent Technologies - Student Management")
    print("=" * 45)

    students = load_students()

    while True:
        print("\n--- Menu ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            search_student(students)
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice! Enter 1-6.")

if __name__ == "__main__":
    main()