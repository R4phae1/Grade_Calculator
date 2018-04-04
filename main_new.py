import json

def loadSetupData():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)
    return course["course_setup"]

def askForAssignmentMarks(grades):
    current_grades = {"mygrades": {}}
    for key in grades:
        print("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")
        k=int(input())
        if (k<0 or k>100) and k!=-1:
            print("Your input is false, input number between 0 and 100")
            askForAssignmentMarks(grades)
        print (current_grades)
    return current_grades

def saveGrades(current_grades):
    file = open("gc_grades.json", "w")
    name=input("What is your name?")
    file.write(name+" "+json.dumps(current_grades))
    file.close()

def printCurrentGrade(grades, current_grades,matrix):
    curr_grade = 0
    for key in current_grades["mygrades"]:
        if current_grades["mygrades"][key] != -1:
            calc_grade = int(current_grades["mygrades"][key]) * grades[key]/100
            curr_grade = curr_grade + calc_grade
            for i in range(len(matrix)):
                if matrix[i]["min"] <= grade and matrix[i]["max"] >= curr_grade:
                    print (matrix[i]["mark"])
        
def main():
    course = loadSetupData()
    grades = course["grade_breakdown"]
    conv_matrix = course["conv_matrix"]
    current_grades = askForAssignmentMarks(grades)
    saveGrades(current_grades)
    curr_grade = printCurrentGrade(grades, current_grades)

main()
