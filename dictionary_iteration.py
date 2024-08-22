student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for name,grade in student_scores.items():
    if grade >= 91 and grade <= 100:
        student_scores[name] = "Outstanding"
    elif grade >= 81 and grade <= 90:
        student_scores[name] = "Exceeds Expectations"
    elif grade >= 71 and grade <= 80:
        student_scores[name] = "Acceptable"
    elif grade <= 70:
        student_scores[name] = "Fail"
        
student_grades = student_scores
        
print(student_grades)