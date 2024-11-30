"""
    Write a function student_score() that takes an integer between 0 and 100
    as input. The function should return
    "A" for scores >= 90, 
    "B" for scores >= 80,
    "C" for scores >= 70,
    "D" for scores >= 60,
    "E" for scores >= 50,
    and "F" for anything below 50.


    Outside the function, write a for-loop that goes from 40 to 100 (inclusive)
    in steps of five. Print the score and the grade. Desired output:

40 F
45 F
50 E
55 E
60 D
65 D
70 C
75 C
80 B
85 B
90 A
95 A
100 A

"""

def student_score(n):
    if n >= 90:
        print(f"{n} A")
    elif n >= 80:
        print(f"{n} B")
    elif n >= 70:
        print(f"{n} C")
    elif n >= 60:
        print(f"{n} D")
    else: 
        print(f"{n} F")
    return n
for i in range(46,105,5):
    #print(i,student_score(i))
    #print(student_score(i))
    student_score(i)   
        #print(student_score(45))
#print(student_score(50))
#print(student_score(55))
#print(student_score(60))
#print(student_score(65))
#print(student_score(70))
#print(student_score(75))
#print(student_score(80))
#print(student_score(85))
#print(student_score(90))
#print(student_score(95))
#print(student_score(100))
