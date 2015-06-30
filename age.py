# A quick and shitty script to solve the problem related to dates of birth, ages and their squares
# as described in numberphile's video https://www.youtube.com/watch?v=99stb2mzspI
# 
# For all yob in range, find all possible values of yob (year of birth)
# such that yob + age = age^2 for a certain value of age
# present solution as a list of tuples
# For example: 1980 + 45 = 2025 = 45^2
# so (1980, 45) is a solution
# f(x, y) => x + y = y^2

def function(x, y):
  if x + y == pow(y, 2):
    return True

while True:

  try:
    n = int(raw_input("Enter start year for year of birth range... "))
    m = int(raw_input("Enter end year for year of birth range... "))
    p = int(raw_input("Enter max human age to compare against... "))

  except ValueError:
    print "You cheeky monkey! You entered something that wasn't quite right!"
    continue

  else:
    break

for yob in range(n, m + 1):
  for age in range(0, p): 
    if function(yob, age):
      print (yob, age), "is a solution because", yob, "+", age, " = ", yob + age, " = ", age, "^2"