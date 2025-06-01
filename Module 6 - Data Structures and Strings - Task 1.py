#student dictionary with names and marks
studentsMarks = {"Alan":99, "Ben":77, "Charlie":100, "Denver":63, "Eugene":81}
def getMarks(s):
    if s in studentsMarks:
        return "{} 's marks: {}".format(s, studentsMarks[s])
    else:
        return "Student not found."

name=input("Enter the student's name: ")
#print(studentsMarks.get(name, "Student not found."))

print(getMarks(name))

