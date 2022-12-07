# organicACSScript.py
# Chad E. Wallace, Ph.d.
# Fall 2022
#
# This program is a script I wrote that analyzes the grade for a senior student at Anderson University
# who takes the 1998 ACS organic chemistry exam as a senior and/or the 2002 ACS organic chemistry
# exam as a student in organic chemistry. The number of questions the student misses is entered
# and this progarm calcualtes the raw score, the percentile ranking, and/or the exam grade as appropriate.

# Initialize some needed variables.

numMissed = 0 # This is how many the student missed out of 70.
raw = 0 # This is the student's raw score out of 70
perc = 0 #  This is the student's national percentile ranking
cont = " "  # input to see if we should continue the program
quit = "q"
exam = ""


# Allow user to select one of the two exams that we use at Anderson University

print("Which exam are we grading?")
print("A: 1994 ACS Exam for senior assessment")
print("B: 1998 ACS Exam for senior assessment")
print("C: 2002 ACS Exam for organic chemistry class final exam")
exam = input()

# Make sure a correct input is used.
while exam != "A" and exam != "a" and exam != "B" and exam != "b":
    print("Incorrect input")
    print("A: 1994 ACS Exam for senior assessment retake exam")
    print("B: 1998 ACS Exam for senior assessment")
    print("C: 2002 ACS Exam for organic chemistry class final exam")
    print("Please enter either A, B, or C. . .")
    exam = input()
# if the user wants to look at the 1994 exam, which we use for senior assessment retakes at AU. . .

if exam == "A" or exam == "a":

# For the 1994 ACS organic exam as an assessment for a senior. Enter the numbr of questions missed from the 1998 ACS organic chemistry exam
# out of 70 points. The program converts that to a raw score and to the national percentile for that
# student. 

    print("\nFor the 1994 ACS Organinc Chemistry Exam\n")

    while (cont != quit):

        #Get the percentile for the students
        print("Enter the number missed out of 70.")
        numMissed = input()
        
        raw = 70 - int(numMissed)

        # convert raw score to percentile for 1998 ACS exam

        if (raw >= 66):
            perc = 100
        elif (raw >= 64):
            perc = 99
        elif (raw >= 62):
            perc = 98
        elif (raw >= 60):
            perc = 97
        elif (raw == 59):
            perc = 96
        elif (raw == 58):
            perc = 95
        elif (raw == 57):
            perc = 93
        elif (raw == 56):
            perc = 92
        elif (raw == 55):
            perc = 90
        elif (raw == 54):
            perc = 89
        elif (raw == 53):
            perc = 87
        elif (raw == 52):
            perc = 86
        elif (raw == 51):
            perc = 83
        elif (raw == 50):
            perc = 82
        elif (raw == 49):
            perc = 80
        elif (raw == 48):
            perc = 78
        elif (raw == 47):
            perc = 75
        elif (raw == 46):
            perc = 73
        elif (raw == 45):
            perc = 70
        elif (raw == 44):
            perc = 67
        elif (raw == 43):
            perc = 65
        elif (raw == 42):
            perc = 62
        elif (raw == 41):
            perc = 59
        elif (raw == 40):
            perc = 56
        elif (raw == 39):
            perc = 53
        elif (raw == 38):
            perc = 49
        elif (raw == 37):
            perc = 46
        elif (raw == 36):
            perc = 43
        elif (raw == 35):
            perc = 39
        elif (raw == 34):
            perc = 36
        elif (raw == 33):
            perc = 33
        elif (raw == 32):
            perc = 29
        elif (raw == 31):
            perc = 26
        elif (raw == 30):
            perc = 24    
        elif (raw == 29):
            perc = 21
        elif (raw == 28):
            perc = 18
        elif (raw == 27):
            perc = 16
        elif (raw == 26):
            perc = 13
        elif (raw == 25):
            perc = 11
        elif (raw == 24):
            perc = 8   
        elif (raw == 23):
            perc = 6
        elif (raw == 22):
            perc = 5
        elif (raw == 21):
            perc = 4
        elif (raw == 20):
            perc = 3
        elif (raw >= 18):
            perc = 2
        elif (raw >= 15):
            perc = 1
        else:
            perc = 0 

        print("The student raw grade is: " + str(raw))
        print("The student perentile ranking is: " + str(perc))
        print("")
        print("To quit hit 'q', else hit any other key.")
        cont = input()

# if the user wants to look at the 1998 exam, which we use for senior assessment. . .

if exam == "B" or exam == "b":

# For the 1998 ACS organic exam as an assessment for a senior. Enter the numbr of questions missed from the 1998 ACS organic chemistry exam
# out of 70 points. The program converts that to a raw score and to the national percentile for that
# student. 

    print("\nFor the 1998 ACS Organinc Chemistry Exam\n")

    while (cont != quit):

        #Get the percentile for the students
        print("Enter the number missed out of 70.")
        numMissed = input()
        
        raw = 70 - int(numMissed)

        # convert raw score to percentile for 1998 ACS exam

        if (raw >= 66):
            perc = 100
        elif (raw >= 63):
            perc = 99
        elif (raw >= 61):
            perc = 98
        elif (raw == 60):
            perc = 97
        elif (raw >= 58):
            perc = 96
        elif (raw == 57):
            perc = 95
        elif (raw == 56):
            perc = 94
        elif (raw == 55):
            perc = 93
        elif (raw == 54):
            perc = 91
        elif (raw == 53):
            perc = 90
        elif (raw == 52):
            perc = 88
        elif (raw == 51):
            perc = 87
        elif (raw == 50):
            perc = 85
        elif (raw == 49):
            perc = 83
        elif (raw == 48):
            perc = 80
        elif (raw == 47):
            perc = 77
        elif (raw == 46):
            perc = 75
        elif (raw == 45):
            perc = 72
        elif (raw == 44):
            perc = 69
        elif (raw == 43):
            perc = 66
        elif (raw == 42):
            perc = 63
        elif (raw == 41):
            perc = 60
        elif (raw == 40):
            perc = 57
        elif (raw == 39):
            perc = 54
        elif (raw == 38):
            perc = 51
        elif (raw == 37):
            perc = 47
        elif (raw == 36):
            perc = 43
        elif (raw == 35):
            perc = 40
        elif (raw == 34):
            perc = 36
        elif (raw == 33):
            perc = 33
        elif (raw == 32):
            perc = 29
        elif (raw == 31):
            perc = 26
        elif (raw == 30):
            perc = 22    
        elif (raw == 29):
            perc = 20
        elif (raw == 28):
            perc = 17
        elif (raw == 27):
            perc = 14
        elif (raw == 26):
            perc = 11
        elif (raw == 25):
            perc = 9  
        elif (raw == 24):
            perc = 6    
        elif (raw == 23):
            perc = 5
        elif (raw == 22):
            perc = 3
        elif (raw == 21):
            perc = 2
        elif (raw >= 19):
            perc = 1
        else:
            perc = 0 

        print("The student raw grade is: " + str(raw))
        print("The student perentile ranking is: " + str(perc))
        print("")
        print("To quit hit 'q', else hit any other key.")
        cont = input()
else:

    # 2002 ACS organic chemistry exam was selected.
    # This part of the program enters the number missed for the 2002 ACS organic chemistry exam
    # out of 70 points. This is for students at the end of their usually sophomore organic chemistry class. 
    # The program converts that raw score to the national percentile for that
    # student. Then, using the curve I set up for this exam, finds the final grade (out of 100)
    # that I assign to the student.  If the student takes the exam and gets 0th percentile, they get a 50.  
    # The 50th percntile grade gets and 80 on the exam. 100th percentile gets 100.

    # Initialize some variables
    numMissed = 0 # This is how many the student missed out of 70.
    raw = 0 # This is the student's raw score out of 70
    perc = 0 #  This is the student's national percentile ranking
    cont = " "
    quit = "q"
    zero = 0
    grade = 0 # grade given to student out of 100

    print("\nFor the 2002 ACS Organinc Chemistry Exam\n")

    # We keep running the program until q is entered to quit.
    while (cont != quit):

        #Get the percentile for the students
        print("Enter the number missed out of 70.")
        numMissed = input()
        
        raw = 70 - int(numMissed)

        # convert raw score to percentile for 2002 ACS exam

        if (raw >= 67):
            perc = 100
        elif (raw == 66):
            perc = 99
        elif (raw == 65):
            perc = 98
        elif (raw == 64):
            perc = 97
        elif (raw == 63):
            perc = 96
        elif (raw == 62):
            perc = 95
        elif (raw == 61):
            perc = 93
        elif (raw == 60):
            perc = 92
        elif (raw == 59):
            perc = 90
        elif (raw == 58):
            perc = 87
        elif (raw == 57):
            perc = 85
        elif (raw == 56):
            perc = 83
        elif (raw == 55):
            perc = 81
        elif (raw == 54):
            perc = 78
        elif (raw == 53):
            perc = 76
        elif (raw == 52):
            perc = 74
        elif (raw == 51):
            perc = 71
        elif (raw == 50):
            perc = 67
        elif (raw == 49):
            perc = 65
        elif (raw == 48):
            perc = 62
        elif (raw == 47):
            perc = 59
        elif (raw == 46):
            perc = 57
        elif (raw == 45):
            perc = 53
        elif (raw == 44):
            perc = 50
        elif (raw == 43):
            perc = 48
        elif (raw == 42):
            perc = 45
        elif (raw == 41):
            perc = 42
        elif (raw == 40):
            perc = 39
        elif (raw == 39):
            perc = 36
        elif (raw == 38):
            perc = 34
        elif (raw == 37):
            perc = 31
        elif (raw == 36):
            perc = 28
        elif (raw == 35):
            perc = 25    
        elif (raw == 34):
            perc = 23
        elif (raw == 33):
            perc = 20
        elif (raw == 32):
            perc = 18
        elif (raw == 31):
            perc = 16
        elif (raw == 30):
            perc = 14   
        elif (raw == 29):
            perc = 12    
        elif (raw == 28):
            perc = 11
        elif (raw == 27):
            perc = 9
        elif (raw == 26):
            perc = 8
        elif (raw == 25):
            perc = 7
        elif (raw == 24):
            perc = 5   
        elif (raw == 23):
            perc = 5
        elif (raw == 22):
            perc = 4
        elif (raw == 21):
            perc = 3
        elif (raw == 20):
            perc = 3 
        elif (raw == 19):
            perc = 2
        elif (raw == 18):
            perc = 1
        elif (raw == 17):
            perc = 1
        elif (raw == 16):
            perc = 1
        else:
            perc = 0 
            print("Something went wrong. . .")


        # There are two straight lines for the "curve". One is 0th percentile (grade of 50) to 50th percentile (grade of 80)
        # The second line is from 50th perentile to 100th percentile (grade of 100)

        if (perc <= 50):
            grade = 0.6 * perc + 50; # slope is up 30 and over 50. y intercept is 50.
        else:
            grade = 0.4 * perc + 60; # slope is up 20 and over 50.

        rndGrade = round(grade,1)
        print("The student raw grade is: " + str(raw))
        print("The student perentile ranking is: " + str(perc))
        print("The student grade is: " + str(rndGrade))
        print("")
        print("To quit hit 'q', else hit any other key.")
        cont = input()
