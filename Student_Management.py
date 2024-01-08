class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f'Student "{student["full_name"]}" added successfully.')

    def show_all_students(self):
        if not self.students:
            print('No students available.')
        else:
            print('All Students:')
            for index, student in enumerate(self.students, start=1):
                print(f'{index}. {student["full_name"]} - ID: {student["id"]} - Age: {student["age"]} - DOB: {student["dob"]} - Class: {student["class"]}')
                print('   Subjects:')
                for subject, marks in student["subjects"].items():
                    print(f'   - {subject}: {marks}')

    def filter_students(self, criteria):
        filtered_students = [student for student in self.students if criteria(student)]
        if not filtered_students:
            print('No students match the criteria.')
        else:
            print('Filtered Students:')
            for index, student in enumerate(filtered_students, start=1):
                print(f'{index}. {student["full_name"]} - ID: {student["id"]} - Age: {student["age"]} - DOB: {student["dob"]} - Class: {student["class"]}')
                print('   Subjects:')
                for subject, marks in student["subjects"].items():
                    print(f'   - {subject}: {marks}')

    def search_student(self, student_name):
        found_students = [student for student in self.students if student["full_name"].lower() == student_name.lower()]
        if not found_students:
            print(f'No student found with the name "{student_name}".')
        else:
            print('Found Students:')
            for index, student in enumerate(found_students, start=1):
                print(f'{index}. {student["full_name"]} - ID: {student["id"]} - Age: {student["age"]} - DOB: {student["dob"]} - Class: {student["class"]}')
                print('   Subjects:')
                for subject, marks in student["subjects"].items():
                    print(f'   - {subject}: {marks}')

    def update_student(self, student_id, new_data):
        for student in self.students:
            if student["id"] == student_id:
                student.update(new_data)
                print(f'Student "{student["full_name"]}" updated successfully.')
                return
        print(f'No student found with ID {student_id}.')

    def delete_student(self, student_id):
        for index, student in enumerate(self.students):
            if student["id"] == student_id:
                deleted_student = self.students.pop(index)
                print(f'Student "{deleted_student["full_name"]}" deleted successfully.')
                return
        print(f'No student found with ID {student_id}.')

def main():
    student_management = StudentManagement()

    while True:
        print('\n1. Add Student\n2. Show All Students\n3. Filter Students\n4. Search Student\n5. Update Student\n6. Delete Student\n7. Quit')
        choice = input('Enter your choice (1/2/3/4/5/6/7): ')

        if choice == '1':
            full_name = input('Enter student full name: ')
            student_id = int(input('Enter student ID: '))
            age = int(input('Enter student age: '))
            dob = input('Enter student date of birth (DOB): ')
            student_class = input('Enter student class: ')
            subjects = {}
            num_subjects = int(input('Enter the number of subjects: '))
            for _ in range(num_subjects):
                subject_name = input('Enter subject name: ')
                subject_marks = float(input('Enter marks in the subject: '))
                subjects[subject_name] = subject_marks

            student = {
                "full_name": full_name,
                "id": student_id,
                "age": age,
                "dob": dob,
                "class": student_class,
                "subjects": subjects
            }

            student_management.add_student(student)
        elif choice == '2':
            student_management.show_all_students()
        elif choice == '3':
            criteria = lambda student: student["age"] >= 18
            student_management.filter_students(criteria)
        elif choice == '4':
            student_name = input('Enter student name to search: ')
            student_management.search_student(student_name)
        elif choice == '5':
            student_id = int(input('Enter student ID to update: '))
            new_full_name = input('Enter new student full name: ')
            new_age = int(input('Enter new student age: '))
            new_dob = input('Enter new student date of birth (DOB): ')
            new_class = input('Enter new student class: ')
            new_subjects = {}
            num_subjects = int(input('Enter the number of subjects: '))
            for _ in range(num_subjects):
                subject_name = input('Enter subject name: ')
                subject_marks = float(input('Enter marks in the subject: '))
                new_subjects[subject_name] = subject_marks

            new_data = {
                "full_name": new_full_name,
                "age": new_age,
                "dob": new_dob,
                "class": new_class,
                "subjects": new_subjects
            }

            student_management.update_student(student_id, new_data)
        elif choice == '6':
            student_id = int(input('Enter student ID to delete: '))
            student_management.delete_student(student_id)
        elif choice == '7':
            print('Exiting program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

if __name__ == "__main__":
    main()
