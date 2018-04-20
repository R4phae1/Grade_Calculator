import json


def setup_data():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)

    grades = course["course_setup"]["grade_breakdown"]
    return grades

def conversion_matrix():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)

    convMatrix = course["course_setup"]["conv_matrix"]
    return convMatrix

def input_name():
    student_name = input("Please type your name. ")
    student_file = student_name.lower()
    return student_file

def old_grades():

    try:
        with open("gc_grades.json") as data_file:
                old_grades = json.load(data_file)
    except:
        file = open("gc_grades.json", "w")
        file.write("{}")
        file.close()
        with open("gc_grades.json") as data_file:
            old_grades = json.load(data_file)


    return old_grades

def askForValidGrade(key):
    current_key = input("What is your Current Grade for: " + key + " Please insert -1 if you don't have a grade yet. ")
    while ((int(current_key) > 100 or int(current_key) < 0) and int(current_key) != -1):
        current_key = input("Wrong input. Please enter a number inbetween 0 and 100 (or -1). ")
    return current_key


def ask_for_grades(grades, old_grades, student_file):

    if str(old_grades).find(student_file) != -1:
        for key in grades:
            if int(old_grades[student_file][key]) < 0:
                current_key = askForValidGrade(key)
            else:
                print ("You already have a grade in " + key + ". Do you want to change? ")
                print (old_grades[student_file][key])
                wantChange = str (input("Would you like to change it? Y/N "))
                while (wantChange != "Y" and wantChange != "N"):
                    wantChange = str(input("Wrong input. Please input Y or N. "))
                if (wantChange == "N"):
                    current_key = old_grades[student_file][key]
                elif (wantChange == "Y"):
                    current_key = askForValidGrade(key)
            old_grades[student_file][key] = current_key
            current_grades = old_grades
    else:
        current_grades = old_grades
        new_grades = {student_file: {}}
        for key in grades:
            current_key = input(
                "What is your Current Grade for: " + key + " Please insert -1 if you don't have a grade yet ")
            while (int(current_key) > 100 or int(current_key)< 0) and int(current_key) != -1:
                current_key = input("Grade must be in between 0 and 100. Or, insert -1 if you don't have a grade yet.")
            new_grades[student_file][key] = current_key

    return current_grades


def save(old_grades):
    file = open("gc_grades.json", "w")
    file.write(json.dumps(old_grades))
    file.close()

def print_grades(grades, convMatrix, current_grades, student_file,):
    final_grade = 0
    for key in current_grades[student_file]:
        if current_grades[student_file][key] != -1:
            calc_grade = (float((current_grades[student_file][key]) * grades[key]) / 100)
            final_grade = final_grade + calc_grade
    print ("Final grade: " + str(final_grade))
    letter_grade = convert(convMatrix, final_grade)
    print ("Letter grade: " + str(letter_grade))
    return final_grade

def convert(convMatrix, final_grade):
    for key in convMatrix:
        max = float(key["max"])
        min = float(key["min"])
        letter_grade=" "
        if (float(max) >= final_grade) and (float(min) < final_grade):
             letter_grade = key["mark"]
    return letter_grade

def main():
    grades = setup_data()
    convMatrix = conversion_matrix()
    student_file = input_name()
    old = old_grades()
    current_grades = ask_for_grades(grades, old, student_file)
    save(current_grades)
    print_grades(grades, convMatrix, current_grades, student_file)

main()
