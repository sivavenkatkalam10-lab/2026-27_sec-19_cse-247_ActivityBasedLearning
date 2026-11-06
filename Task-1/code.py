

eligible_students = []


MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

n = int(input("Enter number of students: "))

for i in range(n):

    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    marks = []

    subjects = int(input("Enter number of subjects: "))

    for j in range(subjects):
        mark = float(input(f"Enter marks in subject {j+1}: "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))
    aggregate = sum(marks) / subjects

    
    if (aggregate >= MIN_AGGREGATE and
        min(marks) >= MIN_SUBJECT_MARKS and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        eligible_students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

        print(name, "is Eligible for Scholarship")

    else:
        print(name, "is Not Eligible for Scholarship")




eligible_students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"],
        x["name"].lower()
    )
)


print("\n===== SCHOLARSHIP RANKING =====")

if eligible_students:

    for rank, student in enumerate(eligible_students, start=1):

        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Aggregate:", student["aggregate"], "%")
        print("Attendance:", student["attendance"], "%")
        print("Family Income: Rs.", student["income"])

else:
    print("No eligible students found.")

