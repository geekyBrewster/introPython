grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  sum = 0
  for score in scores:
    sum = sum + score
  return sum

print grades_sum(grades)

def grades_average(grades_input):
  average = grades_sum(grades_input)/float(len(grades_input))
  return average

print grades_average(grades)

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance = variance + (average - score) ** 2
  return variance / len(scores)

print grades_variance(grades)

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)
print grades_std_deviation(variance)
