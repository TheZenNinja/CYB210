
def getLetterGrade(score):
    if (score >= 90):
        return "A"
    elif (score >= 80):
        return "B"
    elif (score >= 80):
        return "C"
    elif (score >= 80):
        return "D"
    else:
        return "F"


inputScore = float(input("Input Grade: "))
print("Your letter grade is:", getLetterGrade(inputScore))