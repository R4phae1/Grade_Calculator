import json

def setup_data():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)

    grades = course["course_setup"]["grade_breakdown"]
    return grades

def conversion_matrix():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)

    matrix = course["course_setup"]["conv_matrix"]
    return matrix

def input():
    student_name = input("Please type your ID. ")
    #student=bool(input("Are you a new student?"))
    #if student:
        #file = open("gc_grades.json", "r")
        #lines=file.readlines()
       # file.close()
       # file = open("gc_grades.json", "w")
       # file.write(json.dumps(student_name+': {"assignment2": 0, "assignment3": 0, "assignment1": 0, "participation": 0, "assignment4": 0}}'))
        #file.close()
    student_file = student_name.lower()
    return student_file

def old_grades():

    with open("gc_grades.json") as data_file:
        old_grades = json.load(data_file)
    return old_grades

def ask_for_grades(grades, old_grades, student_file):

    if str(old_grades).find(student_file) != -1:
        for key in grades:
            if old_grades[student_file][key] < 0:
                current_key = input(
                    "What is your Current Grade for: " + key + " Please insert -1 if you don't have a grade yet ")
                while (current_key > 100 or current_key < 0) and current_key != -1:
                    current_key = input(
                        "Grade must be in between 0 and 100. Or, insert -1 if you don't have a grade yet.")
            else:
                print ("You already have a grade in " + key + ". Do you want to change? ")
                print (old_grades[student_file][key])
                change = input("Would you like to change it? Y/N ")
                while (change != "Y" and change != "N"):
                    change = input("Wrong input. Please input Y or N. ")
                if (change == "N"):
                    current_key = old_grades[student_file][key]
                elif (change == "Y"):
                    current_key = input(
                        "What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet ")
                    while (current_key > 100 or current_key < 0) and current_key != -1:
                        current_key = input(
                            "Grade must be in between 0 and 100. Or, insert -1 if you don't have a grade yet.")
            old_grades[student_file][key] = current_key
            current_grades = old_grades
    else:
        current_grades = old_grades
        new_grades = {student_file: {}}
        for key in grades:
            current_key = int(input(
                "What is your Current Grade for: " + key + " Please insert -1 if you don't have a grade yet "))
            while (current_key > 100 or current_key < 0) and current_key != -1:
                current_key = input(
                    "Grade must be in between 0 and 100. Or, insert -1 if you don't have a grade yet.")
            new_grades[student_file][key] = current_key
    return current_grades


def save(old_grades):
    file = open("gc_grades.json", "w")
    file.write(json.dumps(old_grades))
    file.close()

def print(grades, matrix, current_grades, student_file,):
    final_grade = 0
    key = 0
    for key in current_grades:
        if current_grades[student_file][key] != -1:
            calc_grade = (float((current_grades[student_file][key]) * grades[key]) / 100)
            final_grade = final_grade + calc_grade
    print ("Final grade: " + str(final_grade))
    letter_grade = convert(matrix, final_grade)
    print ("Letter grade: " + letter_grade)
    return final_grade

def convert(matrix, final_grade):
    for key in matrix:
        max = float(key["max"])
        min = float(key["min"])
        if (float(max) >= final_grade) and (float(min) < final_grade):
             letter_grade = key["mark"]
    return letter_grade

def main():
    grades = setup_data()
    matrix = conversion_matrix()
    student_file = input()
    old_grades = old_grades()
    current_grades = ask_for_grades(grades, old_grades, student_file)
    save(old_grades)
    print(grades, matrix, current_grades, student_file)

main()