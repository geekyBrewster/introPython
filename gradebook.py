lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
students = [lloyd, alice, tyler]

for student in students:
  print student["name"]
  print student["homework"]
  print student["quizzes"]
  print student["tests"]

# Create a function to find the average of provided scores
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

# Get weighted average for a student
def get_average(name):
  homework = average(name['homework'])
  quizzes = average(name['quizzes'])
  tests = average(name['tests'])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

# Assign a letter grade based on student's score
def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

score = get_average(lloyd)
print get_letter_grade(score)

# Get class average
def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

print get_class_average(students)
print get_letter_grade(get_class_average(students))
