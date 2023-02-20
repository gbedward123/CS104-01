howManyEntered = 0
total = 0
average = 0
howMany = int(input("How many test scores would you like to average? "))
testScore = int(input("Enter test score: "))
total = total + testScore
howManyEntered = howManyEntered + 1
while howManyEntered < howMany:
    print(howMany)
    break
average = total / howMany
print("The average for the test scores you entered is: ")
print(average)
