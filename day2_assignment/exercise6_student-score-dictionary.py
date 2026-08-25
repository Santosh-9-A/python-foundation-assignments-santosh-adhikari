'''Create a dictionary containing five students and their scores.

Example:

student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}
Tasks:

Print every student and score.
Create a dictionary containing only students who scored at least 60.
Find the student with the highest score.
Calculate the average score.
Use a dictionary comprehension for the passing students.'''

student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

for key, value in student_scores.items():
    print(f"keys and values: {key, value}")

for student, score in student_scores.items():
    if score>=60:
        print(f"Scores at list 60: {score}")

top_students = max(student_scores, key=student_scores.get)
print(f"Top Student: {top_students}")

average_score = sum(student_scores.values())/ len(student_scores)
print(f"Average Scores: {average_score}")