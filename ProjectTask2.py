class StudentGrades:
    def _init_(self):
        self.subjects = {}

    def add_subject(self, subject_name):
        if subject_name not in self.subjects:
            self.subjects[subject_name] = []
            print(f"Subject '{subject_name}' added.")
        else:
            print(f"Subject '{subject_name}' already exists.")

    def add_grade(self, subject_name, grade):
        if subject_name in self.subjects:
            self.subjects[subject_name].append(grade)
            print(f"Grade {grade} added to subject '{subject_name}'.")
        else:
            print(f"Subject '{subject_name}' does not exist. Please add the subject first.")

    def calculate_average(self, subject_name):
        if subject_name in self.subjects:
            grades = self.subjects[subject_name]
            if grades:
                average = sum(grades) / len(grades)
                return average
            else:
                print(f"No grades recorded for subject '{subject_name}'.")
                return None
        else:
            print(f"Subject '{subject_name}' does not exist.")
            return None

    def calculate_overall_average(self):
        total_sum = 0
        total_count = 0
        for grades in self.subjects.values():
            total_sum += sum(grades)
            total_count += len(grades)
        if total_count == 0:
            print("No grades recorded.")
            return None
        return total_sum / total_count

    def display_all_subjects(self):
        for subject, grades in self.subjects.items():
            print(f"Subject: {subject}, Grades: {grades}, Average: {self.calculate_average(subject):.2f}")

def main():
    student_grades = StudentGrades()

    while True:
        print("\n1. Add Subject")
        print("2. Add Grade")
        print("3. Calculate Subject Average")
        print("4. Calculate Overall Average")
        print("5. Display All Subjects")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            subject_name = input("Enter subject name: ")
            student_grades.add_subject(subject_name)

        elif choice == '2':
            subject_name = input("Enter subject name: ")
            grade = float(input("Enter grade: "))
            student_grades.add_grade(subject_name, grade)

        elif choice == '3':
            subject_name = input("Enter subject name: ")
            average = student_grades.calculate_average(subject_name)
            if average is not None:
                print(f"Average grade for {subject_name}: {average:.2f}")

        elif choice == '4':
            overall_average = student_grades.calculate_overall_average()
            if overall_average is not None:
                print(f"Overall average grade: {overall_average:.2f}")

        elif choice == '5':
            student_grades.display_all_subjects()

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")

if _name_ == "_main_":
    main()
