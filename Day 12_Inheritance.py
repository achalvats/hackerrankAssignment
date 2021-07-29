class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self,firstName, lastName, idNumber)
        self.scores = scores

    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def printPerson(self):
        Person.printPerson(self)
        sum_score = 0
        for score in self.scores:
            sum_score += score
        self.scores_avg = sum_score / len(self.scores)

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        if 100 >= self.scores_avg >= 90:
            return "O"
        elif 90 > self.scores_avg >= 80:
            return "E"
        elif 80 > self.scores_avg >= 70:
            return "A"
        elif 70 > self.scores_avg >= 55:
            return "P"
        elif 55 > self.scores_avg >= 40:
            return "D"
        else:
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
# print(scores)
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
