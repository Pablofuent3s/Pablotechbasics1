import csv
import random


# Step 1
def read_csv(filename):
    students = []  # list to store student data as dictionaries
    try:
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)  # Use DictReader to get rows as dictionaries
            for row in reader:
                students.append(row)  # append each row (student) to the list
        return students

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []  # return empty list if file is missing

# Step 2
def populate_scores(students):
    scores = {}  # This creates an empty dictionary to hold student names and their scores
    for student in students:
        # Use the student name as key
        name = student["Name"]
        # Assign a random score from 1 to 3
        scores[name] = random.randint(1, 3)
    return scores
# Step 3
def calculate_total(scores):
    total = sum(scores.values())  # Add up all the score values
    return total

def calculate_average(scores):
    if scores:
        average = sum(scores.values()) / len(scores)
    else:
        average = 0
    return average
def calculate_all(scores):
    total = calculate_total(scores)      # Use your total function
    average = calculate_average(scores)  # Use your average function

    print(f"Total score of all students: {total}")
    print(f"Average score: {average:.2f}")


# After the update let's save the data as a new csv file

def write_csv(filename, students, scores):
    with open(filename, mode='w', newline='') as file:
        fieldnames = list(students[0].keys()) + ['Score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            name = student.get("Name", "Unknown")
            student_with_score = student.copy()
            student_with_score['Score'] = scores.get(name, 0)
            writer.writerow(student_with_score)

if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        print("Usage: python grade_calculator.py filename.csv")
        exit(1)

    script = argv[0]
    filename = argv[1]

    print("Open file:", filename)

    students = read_csv(filename)
    if not students:
        print("No student data loaded. Exiting.")
        exit()

    scores = populate_scores(students)
    calculate_all(scores)

    user_name = "[your_name]"

    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"
    write_csv(newname, students, scores)
    print("New file written:", newname)

# Run the file with `python grade_calculator.py sheet.csv`