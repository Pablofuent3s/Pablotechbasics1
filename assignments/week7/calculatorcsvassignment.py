import csv
import random
from sys import argv

WEEK_COLUMNS = [f"Week {i}" for i in range(1, 14) if i != 6]

# Step 1
def read_csv(filename):
    students = []  # list to store student data as dictionaries
    try:
        with open(filename, newline='', encoding='utf-8') as file: #we use utf-8 to include special characters
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        return students
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []
# Step 2
def populate_scores(students):
    scores = {}  # This creates an empty dictionary to hold student names and their scores
    for student in students:
        for week in WEEK_COLUMNS:
      students = student["Name"]
        if not student.get(week) or student[week].strip() == "":
            student[week] = str(random.randint(0, 3))
        return students
# Step 3
def calculate_all(students):
    for student in students:
        try:
            scores = [int(student[week]) for week in WEEK_COLUMNS if student[week].strip().isdigit()]
        except ValueError:
            scores = [0 for week in WEEK_COLUMNS]  # if a value cant be converted
        total = sum(sorted(scores, reverse=True)[:10])  # Best 10
        average = round(sum(scores) / len(scores), 2) if scores else 0
        student["Total Points"] = total
        student["Average Points"] = average
    return students


# After the update let's save the data as a new csv file

def write_csv(filename, students):
    if not students:
        print("No student data to write.")
        return
    fieldnames = list(students[0].keys())
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python grade_calculator.py filename.csv")
        exit(1)

    filename = argv[1]
    print("Open file:", filename)

    students = read_csv(filename)
    if not students:
        print("No student data loaded. Exiting.")
        exit()

    students = populate_scores(students)
    students = calculate_totals_and_averages(students)

    user_name = input("Enter your name: ").replace(" ", "_")
    newname = filename.split(".")[0] + f"_calculated_by_{user_name}.csv"
    write_csv(newname, students)
    print("New file written:", newname)