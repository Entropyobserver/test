def student_scores(n):
    if n >= 90:
        return "A"
    if n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    elif n >= 60:
        return "D"
    elif n >= 50:
        return "E"
    return "F"


for i in range(40, 101, 5):
    print(i, student_scores(i))
