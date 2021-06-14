people1 = "lawrence", 25, 'pizza'
people2 = "julia", 23, "tempura"

people = [people1 , people2]

# name, age, food = people
# print(name)
# print(age)
# print(food)

for name, age, food in people:
  print(name)
  print(age)
  print(food)